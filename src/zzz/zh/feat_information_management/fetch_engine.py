"""
合并获取音擎信息：先获取英文名、品阶、detail_url，再获取中文名，最后生成yml文件
"""

import asyncio
import json
import re
import os
from datetime import datetime
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

async def wait_for_network_idle(page, timeout=30000):
    """等待网络空闲"""
    start_time = asyncio.get_event_loop().time()
    while asyncio.get_event_loop().time() - start_time < timeout / 1000:
        try:
            await page.wait_for_load_state("networkidle", timeout=5000)
            break
        except PlaywrightTimeoutError:
            continue

async def scroll_to_load_all_content(page, max_scrolls=50, scroll_delay=4000):
    """滚动页面加载所有懒加载内容"""
    print("\n=== 开始滚动加载所有内容 ===")
    
    initial_count = await page.locator(".tw-flex.tw-p-4.tw-rounded-xl").count()
    print(f"初始卡片数量: {initial_count}")
    
    previous_count = initial_count
    scroll_count = 0
    consecutive_no_change = 0
    
    while scroll_count < max_scrolls:
        try:
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            print(f"第 {scroll_count + 1} 次滚动...")
            
            await page.wait_for_timeout(scroll_delay)
            await wait_for_network_idle(page)
            
            current_count = await page.locator(".tw-flex.tw-p-4.tw-rounded-xl").count()
            if current_count == 0:
                current_count = await page.locator("[class*='tw-flex'][class*='p-4']").count()
            if current_count == 0:
                current_count = await page.locator("[class*='card']").count()
            
            print(f"当前卡片数量: {current_count}")
            
            if current_count == previous_count:
                consecutive_no_change += 1
                if consecutive_no_change >= 3:
                    print("连续3次没有新增内容，停止滚动")
                    break
            else:
                consecutive_no_change = 0
                
            previous_count = current_count
            scroll_count += 1
            
        except Exception as e:
            print(f"滚动过程中出错: {e}")
            break
    
    await page.evaluate("window.scrollTo(0, 0)")
    await page.wait_for_timeout(500)
    
    print(f"滚动完成，共滚动 {scroll_count} 次，最终卡片数量: {previous_count}")
    return previous_count

async def process_card(card, context, index):
    """处理单个卡片，提取音擎信息"""
    try:
        name_elem = card.locator(".tw-font-zzz")
        name = ""
        if await name_elem.count() > 0:
            name = await name_elem.first.text_content()
            name = name.strip() if name else "未知"
        else:
            name = "未知"
        
        print(f"\n=== 处理第 {index} 个卡片: {name} ===")
        
        new_page_event = asyncio.Event()
        found_page = None
        
        async def handle_new_page(page):
            nonlocal found_page, new_page_event
            try:
                await page.wait_for_load_state("domcontentloaded", timeout=10000)
                if "/entry/" in page.url:
                    found_page = page
                    new_page_event.set()
            except:
                pass
        
        context.on("page", handle_new_page)
        
        try:
            await card.click()
            
            try:
                await asyncio.wait_for(new_page_event.wait(), timeout=15)
            except asyncio.TimeoutError:
                print(f"✗ 第 {index} 个卡片 - 超时未找到新页面")
                return {
                    "success": False,
                    "index": index,
                    "card": card,
                    "name": name,
                    "data": None
                }
            
            if found_page:
                url = found_page.url
                match = re.search(r'/entry/(\d+)', url)
                if match:
                    entry_id = match.group(1)
                    detail_url = f"https://wiki.hoyolab.com/pc/zzz/entry/{entry_id}?lang=en-us"
                    print(f"✓ 第 {index} 个卡片 - 成功提取entry_id: {entry_id}")
                    
                    await found_page.close()
                else:
                    print(f"✗ 第 {index} 个卡片 - URL中未找到entry_id")
                    if found_page != context.pages[0]:
                        await found_page.close()
                    return {
                        "success": False,
                        "index": index,
                        "card": card,
                        "name": name,
                        "data": None
                    }
            else:
                print(f"✗ 第 {index} 个卡片 - 未找到新页面")
                return {
                    "success": False,
                    "index": index,
                    "card": card,
                    "name": name,
                    "data": None
                }
        finally:
            context.remove_listener("page", handle_new_page)
        
        # 正确的稀有度获取逻辑：从带有 alt="rarity" 的 img 标签的 src 中提取
        rarity_num = ""
        rarity_elem = card.locator("img[alt='rarity']")
        if await rarity_elem.count() > 0:
            src = await rarity_elem.first.get_attribute("src")
            if src:
                # 从 src 中提取文件名（如 "/_nuxt/img/other_s.6038bbd.png" -> "other_s"）
                filename = src.split('/')[-1].split('.')[0]
                # 根据文件名映射稀有度（直接使用字母）
                rarity_filename_map = {
                    "other_s": "S",  # S级
                    "other_a": "A",  # A级
                    "other_b": "B",  # B级
                    "other_c": "C"   # C级
                }
                rarity_num = rarity_filename_map.get(filename, "")
        
        print(f"  稀有度获取结果: {rarity_num} (src: {src if src else '未找到'})")
        
        attr_elem = card.locator(".tw-w-8.tw-h-8")
        attr = ""
        if await attr_elem.count() > 0:
            attr = await attr_elem.first.get_attribute("class")
        
        attr_name = ""
        if attr:
            if "physics" in attr.lower():
                attr_name = "物理"
            elif "fire" in attr.lower():
                attr_name = "火"
            elif "electric" in attr.lower():
                attr_name = "电"
            elif "ice" in attr.lower():
                attr_name = "冰"
            elif "ether" in attr.lower():
                attr_name = "以太"
        
        # 输出调试信息
        print(f"  ├─ 英文名: {name}")
        print(f"  ├─ 品级: {rarity_num}")
        print(f"  ├─ 属性: {attr_name}")
        print(f"  └─ detail_url: {detail_url}")
        
        return {
            "success": True,
            "index": index,
            "card": None,
            "name": name,
            "data": {
                "index": index,
                "name": name,
                "rarity": rarity_num,
                "attribute": attr_name,
                "entry_id": entry_id,
                "detail_url": detail_url
            }
        }
        
    except Exception as e:
        print(f"处理卡片时出错: {e}")
        return {
            "success": False,
            "index": index,
            "card": card,
            "name": "未知",
            "data": None
        }

async def fetch_engine_detail_urls_inner():
    """内部函数：执行实际的音擎数据获取"""
    
    en_url = "https://wiki.hoyolab.com/pc/zzz/aggregate/11?lang=en-us"
    engine_data = []
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--window-size=1920,1080",
                "--disable-gpu",
                "--no-sandbox",
                "--disable-dev-shm-usage",
            ]
        )
        
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            locale="en-US",
        )
        
        page = await context.new_page()
        page.set_default_timeout(180000)
        
        try:
            print("访问英文版音擎列表页面...")
            await page.goto(en_url, wait_until="domcontentloaded")
            print("等待页面DOM加载完成...")
            await page.wait_for_timeout(10000)
            print("等待网络空闲...")
            await wait_for_network_idle(page)
            
            print("等待卡片容器...")
            try:
                await page.wait_for_selector(".tw-grid", timeout=30000)
                print("找到卡片容器")
            except PlaywrightTimeoutError:
                print("未找到卡片容器")
            
            await page.wait_for_timeout(5000)
            
            await scroll_to_load_all_content(page)
            
            cards = page.locator(".tw-flex.tw-p-4.tw-rounded-xl")
            total_cards = await cards.count()
            print(f"\n找到 {total_cards} 个卡片")
            
            results = [None] * total_cards
            failed_tasks = []
            
            print("\n=== 开始串行处理卡片 ===")
            
            for i in range(total_cards):
                card = cards.nth(i)
                index = i + 1
                result = await process_card(card, context, index)
                
                if result["success"]:
                    results[index - 1] = result["data"]
                else:
                    failed_tasks.append(result)
                
                await asyncio.sleep(1)
            
            success_count = sum(1 for r in results if r is not None)
            fail_count = len(failed_tasks)
            print(f"\n串行处理完成: 成功 {success_count} 个, 失败 {fail_count} 个")
            
            if fail_count > 0:
                print(f"\n=== 开始重试失败的任务（最多5次） ===")
                max_retries = 5
                
                for retry_num in range(max_retries):
                    if not failed_tasks:
                        break
                    
                    print(f"\n--- 第 {retry_num + 1} 次重试 ---")
                    current_failed = failed_tasks.copy()
                    failed_tasks = []
                    
                    for task in current_failed:
                        print(f"\n重试第 {task['index']} 个卡片: {task['name']}")
                        result = await process_card(task["card"], context, task["index"])
                        
                        if result["success"]:
                            results[task["index"] - 1] = result["data"]
                            print(f"✓ 重试成功")
                        else:
                            failed_tasks.append(result)
                            print(f"✗ 重试失败")
                    
                    success_count = sum(1 for r in results if r is not None)
                    fail_count = len(failed_tasks)
                    print(f"第 {retry_num + 1} 次重试完成: 成功 {success_count} 个, 仍失败 {fail_count} 个")
            
            success_count = sum(1 for r in results if r is not None)
            fail_count = len(failed_tasks)
            print(f"\n=== 最终结果 ===")
            print(f"总卡片数: {total_cards}")
            print(f"成功: {success_count} 个")
            print(f"失败: {fail_count} 个")
            
            if fail_count > 0:
                print("\n失败的卡片:")
                for task in failed_tasks:
                    print(f"  - 第 {task['index']} 个: {task['name']}")
            
            engine_data = [r for r in results if r is not None]
            engine_data.sort(key=lambda x: x["index"])
            
            output_file = "engines_en_updated.json"
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(engine_data, f, ensure_ascii=False, indent=2)
            
            print(f"\n结果已保存到 {output_file}")
            
            return engine_data, True
            
        except Exception as e:
            print(f"出错: {e}")
            import traceback
            traceback.print_exc()
            return None, False
        finally:
            await browser.close()
            print("浏览器已关闭")

async def fetch_engine_detail_urls():
    """获取音擎的detail_url（带重试机制）"""
    
    max_retries = 3  # 最大重试次数
    retry_delay = 5  # 基础重试延迟（秒）
    
    for attempt in range(max_retries):
        print(f"\n=== 第 {attempt + 1} 次尝试获取音擎数据 ===")
        
        engine_data, success = await fetch_engine_detail_urls_inner()
        
        if success and engine_data:
            print(f"\n✓ 第 {attempt + 1} 次尝试成功")
            return engine_data
        
        if attempt < max_retries - 1:
            # 指数退避等待
            wait_time = retry_delay * (2 ** attempt)
            print(f"\n第 {attempt + 1} 次尝试失败，等待 {wait_time} 秒后重试...")
            await asyncio.sleep(wait_time)
    
    print(f"\n✗ 已尝试 {max_retries} 次，均失败")
    return None

async def fetch_with_browser(browser_tasks, browser_index, retry_mode=False):
    """单个浏览器实例处理一批任务"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--window-size=1920,1080",
                "--disable-gpu",
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-software-rasterizer",
                "--disable-extensions",
            ]
        )
        
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            locale="zh-CN",
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        
        page = await context.new_page()
        page.set_default_timeout(60000)  # 增加超时时间到60秒
        
        results = []
        
        try:
            for task in browser_tasks:
                detail_url = task["detail_url"]
                index = task["index"]
                name = task["english_name"] if retry_mode else task["name"]
                
                chinese_url = detail_url.replace('lang=en-us', 'lang=zh-cn')
                
                try:
                    # 请求前添加随机延迟，避免被限流
                    await page.wait_for_timeout(500 + (1000 if retry_mode else 0))
                    
                    await page.goto(chinese_url, wait_until='domcontentloaded')
                    await page.wait_for_load_state('networkidle', timeout=30000)
                    await page.wait_for_timeout(1500)
                    
                    title = await page.title()
                    
                    match = re.match(r'(.+?)\s*-\s*HoYoWiki', title)
                    if match:
                        chinese_name = match.group(1).strip()
                        chinese_name = re.sub(r'\s*-\s*绝区零\s*$', '', chinese_name)
                        if chinese_name and len(chinese_name) > 1 and chinese_name != 'Welcome to HoYoWiki':
                            if retry_mode:
                                print(f"  ✓ 重试 浏览器{browser_index} 第 {index} 个: {name} -> {chinese_name}")
                            else:
                                print(f"✓ 浏览器{browser_index} 第 {index} 个: {name} -> {chinese_name}")
                            results.append({
                                "success": True,
                                "index": index,
                                "english_name": name,
                                "chinese_name": chinese_name,
                                "detail_url": detail_url,
                                "chinese_url": chinese_url
                            })
                            continue
                    
                    if retry_mode:
                        print(f"  ✗ 重试 浏览器{browser_index} 第 {index} 个: {name} - 未获取到中文名称")
                    else:
                        print(f"✗ 浏览器{browser_index} 第 {index} 个: {name} - 未获取到中文名称")
                    results.append({
                        "success": False,
                        "index": index,
                        "english_name": name,
                        "chinese_name": "",
                        "detail_url": detail_url,
                        "chinese_url": chinese_url
                    })
                
                except PlaywrightTimeoutError:
                    if retry_mode:
                        print(f"  ✗ 重试 浏览器{browser_index} 第 {index} 个: {name} - 超时")
                    else:
                        print(f"✗ 浏览器{browser_index} 第 {index} 个: {name} - 超时")
                    results.append({
                        "success": False,
                        "index": index,
                        "english_name": name,
                        "chinese_name": "",
                        "detail_url": detail_url,
                        "chinese_url": ""
                    })
                except Exception as e:
                    if retry_mode:
                        print(f"  ✗ 重试 浏览器{browser_index} 第 {index} 个: {name} - 出错: {e}")
                    else:
                        print(f"✗ 浏览器{browser_index} 第 {index} 个: {name} - 出错: {e}")
                    results.append({
                        "success": False,
                        "index": index,
                        "english_name": name,
                        "chinese_name": "",
                        "detail_url": detail_url,
                        "chinese_url": ""
                    })
            
        finally:
            await page.close()
            await context.close()
            await browser.close()
        
        return results

async def run_with_semaphore(semaphore, browser_tasks, browser_index, retry_mode=False):
    """使用信号量限制并发浏览器数量"""
    async with semaphore:
        return await fetch_with_browser(browser_tasks, browser_index, retry_mode)

async def fetch_all_chinese_names(engine_data):
    """异步获取所有音擎的中文名称（整合重试机制，最多100轮）"""
    
    total_items = len(engine_data)
    print(f"\n共 {total_items} 个音擎需要处理中文名")
    
    max_concurrent_browsers = 10  # 最大并发浏览器数
    semaphore = asyncio.Semaphore(max_concurrent_browsers)
    
    # 初始化待处理任务列表
    pending_tasks = []
    for item in engine_data:
        pending_tasks.append({
            "detail_url": item["detail_url"],
            "index": item["index"],
            "name": item["name"]
        })
    
    success_results = []
    max_rounds = 100
    
    for round_num in range(max_rounds):
        if not pending_tasks:
            break
        
        current_round = round_num + 1
        print(f"\n=== 第 {current_round} 轮：处理 {len(pending_tasks)} 个任务 ===")
        
        num_browsers = min(len(pending_tasks), max_concurrent_browsers)
        items_per_browser = (len(pending_tasks) + num_browsers - 1) // num_browsers
        
        if current_round == 1:
            print(f"将创建 {num_browsers} 个浏览器实例（最大并发数: {max_concurrent_browsers}），平均每个处理约 {items_per_browser} 个任务")
            for i in range(num_browsers):
                start = i * items_per_browser
                end = min(start + items_per_browser, len(pending_tasks))
                print(f"  浏览器{i+1} 处理任务: 第 {pending_tasks[start]['index']}-{pending_tasks[end-1]['index']} 个（共 {end-start} 个）")
        
        browser_task_groups = []
        for i in range(num_browsers):
            start = i * items_per_browser
            end = min(start + items_per_browser, len(pending_tasks))
            browser_task_groups.append(pending_tasks[start:end])
        
        browser_tasks = []
        for i, browser_tasks_list in enumerate(browser_task_groups):
            task = asyncio.create_task(run_with_semaphore(semaphore, browser_tasks_list, i + 1, retry_mode=(current_round > 1)))
            browser_tasks.append(task)
        
        all_results = await asyncio.gather(*browser_tasks)
        
        round_results = []
        for browser_result in all_results:
            round_results.extend(browser_result)
        
        new_success = [r for r in round_results if r["success"]]
        pending_tasks = [r for r in round_results if not r["success"]]
        success_results.extend(new_success)
        
        print(f"本轮成功: {len(new_success)} 个")
        print(f"仍失败: {len(pending_tasks)} 个")
        
        # 如果还有失败的任务且不是最后一轮，等待后继续
        if pending_tasks and current_round < max_rounds:
            wait_time = min(3 * current_round, 30)
            print(f"\n等待{wait_time}秒后进行下一轮...")
            await asyncio.sleep(wait_time)
    
    success_count = len(success_results)
    fail_count = len(pending_tasks)
    found_chinese_count = sum(1 for r in success_results if r["chinese_name"])
    
    print(f"\n=== 最终结果 ===")
    print(f"成功请求: {success_count} 个")
    print(f"获取到中文名称: {found_chinese_count} 个")
    print(f"请求失败: {fail_count} 个")
    
    for result in success_results:
        for item in engine_data:
            if item["index"] == result["index"]:
                item["chinese_name"] = result["chinese_name"]
                item["chinese_url"] = result["chinese_url"]
                break
    
    output_file = "engines_with_chinese.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(engine_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n结果已保存到 {output_file}")
    
    return engine_data

def generate_yml_files(engine_data, output_dir="engine_weapon"):
    """为每个音擎生成yml文件"""
    # 获取项目根目录（.debug的上级目录）
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(project_root, output_dir)
    os.makedirs(output_path, exist_ok=True)
    
    for item in engine_data:
        chinese_name = item.get("chinese_name", item.get("name", "未知"))
        rarity_num = item.get("rarity", "")
        
        # 稀有度已经是字母格式（S/A/B/C），直接使用
        # 如果为空则默认设为"B"
        rarity = rarity_num if rarity_num else "B"
        
        english_name = item.get("name", "未知")
        
        # 使用英文名作为文件名（code）
        file_name = f"{english_name}.yml"
        file_path = os.path.join(output_path, file_name)
        
        yml_content = f"""weapon_name: {chinese_name}
rarity: {rarity}
code: "{english_name}"
"""
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(yml_content)
        
        print(f"已生成: {file_path}")
    
    print(f"\n共生成 {len(engine_data)} 个yml文件")

async def main():
    """主函数：先获取detail_url，再获取中文名，最后生成yml文件"""
    
    # 获取今天的日期（格式：YYYY-M-D）
    today = datetime.now()
    date_str = f"{today.year}-{today.month}-{today.day}"
    data_file = f"engines_data_{date_str}.json"
    
    print(f"今日日期: {date_str}")
    print(f"数据文件: {data_file}")
    
    # 检查是否存在今日的数据文件
    if os.path.exists(data_file):
        print(f"\n=== 发现今日数据文件，跳过第一步 ===")
        with open(data_file, "r", encoding="utf-8") as f:
            engine_data = json.load(f)
        print(f"已从 {data_file} 加载 {len(engine_data)} 条数据")
    else:
        print("=== 第一步：获取音擎的英文名、品阶、detail_url ===")
        engine_data = await fetch_engine_detail_urls()
        
        if not engine_data:
            print("未获取到音擎数据，程序退出")
            return
        
        # 保存为日期命名的json文件
        with open(data_file, "w", encoding="utf-8") as f:
            json.dump(engine_data, f, ensure_ascii=False, indent=2)
        print(f"\n数据已保存到 {data_file}")
    
    print("\n=== 第二步：获取音擎的中文名称 ===")
    engine_data = await fetch_all_chinese_names(engine_data)
    
    print("\n=== 第三步：生成yml文件 ===")
    generate_yml_files(engine_data)
    
    print("\n=== 全部完成 ===")

if __name__ == "__main__":
    asyncio.run(main())