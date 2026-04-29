#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
爬取萌娘百科绝区零驱动盘数据
来源：https://mzh.moegirl.org.cn/%E7%BB%9D%E5%8C%BA%E9%9B%B6/%E9%A9%B1%E5%8A%A8%E7%9B%98
输出：YAML格式文件，存储在 drive_disk 文件夹中
"""

import requests
from bs4 import BeautifulSoup
import os
import re
import time


def fetch_drive_disk_data():
    """抓取驱动盘数据"""
    url = "https://mzh.moegirl.org.cn/%E7%BB%9D%E5%8C%BA%E9%9B%B6/%E9%A9%B1%E5%8A%A8%E7%9B%98"
    delay = 3  # 请求间隔，避免被风控
    
    # 创建Session对象，维持连接
    session = requests.Session()
    
    # 设置更多请求头信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://mzh.moegirl.org.cn/',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1'
    }
    session.headers.update(headers)
    
    try:
        print(f"正在抓取驱动盘数据: {url}")
        
        # 先访问主页获取Cookie
        print("  正在获取初始Cookie...")
        session.get('https://mzh.moegirl.org.cn/', timeout=30)
        time.sleep(delay)
        
        # 添加延迟避免频繁请求
        time.sleep(delay)
        
        # 发送请求
        response = session.get(url, timeout=30)
        response.encoding = 'utf-8'
        
        print(f"响应状态码: {response.status_code}")
        
        # 检查是否被限流
        if response.status_code == 429:
            print('访问太频繁，自动暂停120s')
            time.sleep(120)
            # 重新请求
            response = session.get(url, timeout=30)
            response.encoding = 'utf-8'
        
        if response.status_code != 200:
            print(f"请求失败，状态码: {response.status_code}")
            print("尝试调整请求头后重试...")
            
            # 尝试调整User-Agent
            session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            time.sleep(delay)
            
            response = session.get(url, timeout=30)
            response.encoding = 'utf-8'
            
            print(f"重试响应状态码: {response.status_code}")
            
            if response.status_code != 200:
                print("无法从URL获取数据")
                return None, None
        
        # 检查响应内容类型，处理可能的压缩
        content_encoding = response.headers.get('Content-Encoding', '')
        print(f"响应头 Content-Encoding: {content_encoding}")
        print(f"响应头 Content-Type: {response.headers.get('Content-Type')}")
        
        # 根据压缩方式解压内容
        raw_content = response.content
        try:
            if 'br' in content_encoding:
                import brotli
                html_content = brotli.decompress(raw_content).decode('utf-8')
                print("使用 Brotli 解压成功")
            elif 'gzip' in content_encoding:
                import gzip
                html_content = gzip.decompress(raw_content).decode('utf-8')
                print("使用 gzip 解压成功")
            elif 'deflate' in content_encoding:
                import zlib
                html_content = zlib.decompress(raw_content, zlib.MAX_WBITS | 16).decode('utf-8')
                print("使用 zlib 解压成功")
            else:
                html_content = response.text
                print("无需解压")
        except Exception as e:
            print(f"解压失败: {e}")
            html_content = response.text
        
        print(f"响应内容长度: {len(html_content)}")
        
        # 保存获取到的HTML内容用于调试
        debug_file = r"d:\my\project\zzz_drive-disk-rating\.debug\debug_page.html"
        with open(debug_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"页面内容已保存到: {debug_file}")
        
        # 打印前200个字符用于调试
        print(f"页面前200字符: {repr(html_content[:200])}")
        
        # 使用html.parser解析器（更稳定）
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 调试：查看页面中的所有表格
        tables = soup.find_all('table')
        print(f"页面中找到 {len(tables)} 个表格")
        for idx, t in enumerate(tables):
            attrs = str(t.attrs)[:100]
            print(f"  表格{idx}: {attrs}")
        
        # ========== 提取驱动盘数据（第一个wikitable表格） ==========
        drive_disks = []
        wikitable_tables = soup.find_all('table', class_='wikitable')
        
        if wikitable_tables:
            table = wikitable_tables[0]
            print(f"\n[驱动盘数据] 找到表格，属性: {table.attrs}")
            
            # 尝试使用正则表达式从HTML字符串中提取驱动盘数据
            print("使用正则表达式提取驱动盘数据...")
            
            # 匹配驱动盘数据的正则表达式
            drive_disk_pattern = re.compile(
                r'<td rowspan="2">.*?</td>\s*'  # 图片单元格（可能包含figure标签）
                r'<td rowspan="2">([^<]+?)</td>\s*'  # 名称
                r'<td>([^<]+?)</td>\s*'  # 2件套效果
                r'<td rowspan="2">([^<]+?)</td></tr>\s*'  # 简介
                r'<tr>\s*<td>([^<]+?)</td></tr>',  # 4件套效果
                re.DOTALL
            )
            
            matches = drive_disk_pattern.findall(str(table))
            print(f"找到 {len(matches)} 个驱动盘匹配")
            
            for match in matches:
                name = match[0].strip().replace('\n', '').replace('\r', '')
                effect2 = match[1].strip().replace('\n', '').replace('\r', '')
                description = match[2].strip().replace('\n', '').replace('\r', '')
                effect4 = match[3].strip().replace('\n', '').replace('\r', '')
                
                if name:
                    drive_disk = {
                        'name': name,
                        'effect_2set': effect2,
                        'effect_4set': effect4,
                        'description': description,
                        'image_url': None
                    }
                    drive_disks.append(drive_disk)
                    print(f"  已提取驱动盘: {name}")
        
        print(f"\n成功提取 {len(drive_disks)} 个驱动盘")
        
        # ========== 提取驱动盘搭配推荐数据（包含"怪兽与怪客"等内容的表格） ==========
        drive_disk_combinations = []
        
        # 在所有表格中查找包含"怪兽与怪客"的表格
        for table in tables:
            table_str = str(table)
            if '怪兽与怪客' in table_str or '驱动盘' in table_str:
                # 使用正则表达式提取搭配数据
                # 格式：<tr><td>搭配名称</td><td>怪物</td><td>驱动盘组合</td></tr>
                combination_pattern = re.compile(
                    r'<tr>\s*<td>([^<]+?)</td>\s*<td>(.+?)</td>\s*<td>([^<]+?)</td>\s*</tr>',
                    re.DOTALL
                )
                
                matches = combination_pattern.findall(table_str)
                if len(matches) > 3:  # 排除小表格
                    print(f"\n[搭配推荐] 找到包含 {len(matches)} 条搭配的表格")
                    
                    for match in matches:
                        combo_name = match[0].strip().replace('\n', '').replace('\r', '')
                        monsters = match[1].strip().replace('\n', '').replace('\r', '')
                        disks = match[2].strip().replace('\n', '').replace('\r', '')
                        
                        # 清理怪物名称（移除链接标签）
                        monsters_clean = re.sub(r'<[^>]+>', '', monsters)
                        monsters_clean = re.sub(r'\s+', ' ', monsters_clean).strip()
                        
                        if combo_name and disks:
                            # 拆分驱动盘组合
                            disk_list = [d.strip() for d in disks.split('、') if d.strip()]
                            
                            combination = {
                                'name': combo_name,
                                'monsters': monsters_clean,
                                'drive_disks': disk_list
                            }
                            drive_disk_combinations.append(combination)
                            print(f"  已提取搭配: {combo_name} -> {', '.join(disk_list)}")
                    break
        
        print(f"\n成功提取 {len(drive_disk_combinations)} 条驱动盘搭配推荐")
        
        return drive_disks, drive_disk_combinations
    
    except Exception as e:
        print(f"抓取失败: {str(e)}")
        import traceback
        traceback.print_exc()
        return None, None


def convert_to_code(name):
    """将中文名称转换为code格式（混合策略：特殊名称手动映射 + 普通名称拼音转换）"""
    # 特殊名称的手动映射（包含所有已知驱动盘）
    special_cases = {
        # 重金属系列
        '混沌重金属': 'chaos_heavy_metal',
        '獠牙重金属': 'fang_heavy_metal',
        '雷暴重金属': 'thunder_heavy_metal',
        '炎狱重金属': 'inferno_heavy_metal',
        '极地重金属': 'polar_heavy_metal',
        
        # 爵士系列
        '摇摆爵士': 'swing_jazz',
        '混沌爵士': 'chaos_jazz',
        '自由爵士': 'free_jazz',
        
        # 朋克系列
        '激素朋克': 'hormone_punk',
        '原始朋克': 'primitive_punk',
        
        # 迪斯科系列
        '震星迪斯科': 'shocking_disco',
        
        # 电音系列
        '啄木鸟电音': 'woodpecker_electronic',
        '河豚电音': 'pufferfish_electronic',
        
        # 其他
        '灵魂摇滚': 'soul_rock',
        '自由蓝调': 'free_blues',
        '折枝剑歌': 'broken_branch_sword_song',
        '静听嘉音': 'silent_listen_jia_yin',
        '如影相随': 'shadow_follower',
        '法厄同之歌': 'song_of_phoebus',
        '云岿如我': 'cloud_mountain_self',
        '山大王': 'mountain_lord',
        '拂晓生花': 'dawn_blossom',
        '月光骑士颂': 'moonlight_knight_ode',
        '雪兔梦游仙境': 'snow_rabbit_wonderland',
        '囚徒手记': 'prisoners_notebook',
        '沧浪行歌': 'canglang_song',
        '流光咏叹': 'flowing_light_aria'
    }
    
    # 优先检查特殊映射
    if name in special_cases:
        return special_cases[name]
    
    # 默认使用拼音转换
    try:
        from pypinyin import lazy_pinyin
        pinyin_parts = lazy_pinyin(name)
        code = '_'.join(pinyin_parts).lower()
        # 移除特殊字符
        code = re.sub(r'[^a-z0-9_]', '', code)
        return code
    except ImportError:
        # 如果没有安装pypinyin，回退到简单处理
        code = re.sub(r'[\s]+', '_', name.strip())
        code = re.sub(r'_+', '_', code)
        return code.strip('_').lower()


def save_as_yaml(drive_disks, output_dir):
    """将驱动盘数据保存为YAML文件"""
    os.makedirs(output_dir, exist_ok=True)
    
    for disk in drive_disks:
        code = convert_to_code(disk['name'])
        filename = f"{code}.yml"
        filepath = os.path.join(output_dir, filename)
        
        # 获取 mission_type_name（优先使用驱动盘数据中的值，默认为"怪物与怪客"）
        mission_type = disk.get('mission_type_name', '怪物与怪客')
        
        # YAML格式
        yaml_content = f'set_name: "{disk["name"]}"\n'
        yaml_content += f'mission_type_name: "{mission_type}"\n'
        yaml_content += f'code: {code}\n'
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(yaml_content)
        
        print(f"  已保存: {filename}")


def main():
    """主函数"""
    print("=" * 60)
    print("爬取绝区零驱动盘数据")
    print("=" * 60)
    
    # 1. 抓取数据
    print("\n[步骤1] 抓取驱动盘数据")
    drive_disks, drive_disk_combinations = fetch_drive_disk_data()
    
    if not drive_disks:
        drive_disks = []  # 初始化空列表
    
    # 2. 根据搭配数据补充驱动盘数据
    print("\n[步骤2] 根据搭配推荐补充驱动盘数据")
    if drive_disk_combinations:
        # 创建已存在的驱动盘名称集合
        existing_names = {disk['name'] for disk in drive_disks}
        
        # 从搭配推荐中提取所有驱动盘
        disk_to_mission = {}
        for combo in drive_disk_combinations:
            mission_name = combo['name']
            for disk_name in combo['drive_disks']:
                disk_to_mission[disk_name] = mission_name
                
                # 如果驱动盘不存在，则创建新的驱动盘数据
                if disk_name not in existing_names:
                    new_disk = {
                        'name': disk_name,
                        'effect_2set': '',
                        'effect_4set': '',
                        'description': '',
                        'image_url': None,
                        'mission_type_name': mission_name
                    }
                    drive_disks.append(new_disk)
                    existing_names.add(disk_name)
                    print(f"  从搭配推荐补充: {disk_name} -> {mission_name}")
        
        # 更新已存在驱动盘的 mission_type_name
        for disk in drive_disks:
            if disk['name'] in disk_to_mission:
                disk['mission_type_name'] = disk_to_mission[disk['name']]
            else:
                disk['mission_type_name'] = "怪物与怪客"  # 默认值
    
    # 3. 保存驱动盘数据
    print("\n[步骤3] 保存驱动盘为YAML文件")
    output_dir = r"d:\my\project\zzz_drive-disk-rating\.debug\drive_disk"
    save_as_yaml(drive_disks, output_dir)
    
    # 4. 保存搭配推荐数据
    if drive_disk_combinations:
        print("\n[步骤4] 保存驱动盘搭配推荐")
        combinations_file = r"d:\my\project\zzz_drive-disk-rating\.debug\drive_disk_combinations.yml"
        save_combinations_as_yaml(drive_disk_combinations, combinations_file)
    
    # 5. 打印摘要
    print("\n" + "=" * 60)
    print("完成摘要")
    print("=" * 60)
    print(f"共抓取/补充 {len(drive_disks)} 个驱动盘")
    print(f"共提取 {len(drive_disk_combinations)} 条搭配推荐")
    print(f"输出目录: {output_dir}")
    print("\n驱动盘列表:")
    for disk in sorted(drive_disks, key=lambda x: x['name']):
        mission = disk.get('mission_type_name', '怪物与怪客')
        print(f"  - {disk['name']} ({mission})")


def save_combinations_as_yaml(combinations, filepath):
    """将驱动盘搭配推荐保存为YAML文件"""
    yaml_content = "# 驱动盘搭配推荐\n"
    yaml_content += "# 格式: 搭配名称 -> [推荐驱动盘1, 推荐驱动盘2]\n\n"
    
    for combo in combinations:
        yaml_content += f"- name: \"{combo['name']}\"\n"
        yaml_content += f"  monsters: \"{combo['monsters']}\"\n"
        yaml_content += "  drive_disks:\n"
        for disk in combo['drive_disks']:
            yaml_content += f"    - \"{disk}\"\n"
        yaml_content += "\n"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(yaml_content)
    
    print(f"  已保存搭配推荐: {os.path.basename(filepath)}")


if __name__ == '__main__':
    main()