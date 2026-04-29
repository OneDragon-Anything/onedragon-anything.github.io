#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
爬取角色数据并转换为指定格式（异步版本）
"""

import json
import os
import time
import re
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import quote

# 属性映射
ELEMENT_MAP = {
    '电': 'ELECTRIC',
    '以太': 'ETHEREAL',
    '物理': 'PHYSICAL',
    '冰': 'ICE',
    '凛刃': 'FROST',
    '火': 'FIRE',
}

# 默认角色类型映射（根据属性推断）
ELEMENT_TO_AGENT_TYPE = {
    'ELECTRIC': 'STUN',
    'ETHEREAL': 'BUFF',
    'PHYSICAL': 'ATK',
    'ICE': 'FREEZE',
    'FROST': 'ATK',
    'FIRE': 'BURNING',
    'WIND': 'ATK',
    'VOID': 'ATK'
}

# 并发控制
MAX_CONCURRENT_REQUESTS = 10

def load_character_data(json_path='character_data.json'):
    """从JSON文件加载角色数据"""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"加载角色数据失败: {str(e)}")
        return None

def extract_character_names(character_images):
    """从图片名称中提取角色名"""
    character_names = []
    for img_name in character_images:
        # 去掉 "角色-" 前缀和 ".png" 后缀
        if img_name.startswith('角色-') and img_name.endswith('.png'):
            char_name = img_name[3:-4]  # 去掉前缀和后缀
            character_names.append(char_name)
    return character_names

async def extract_character_names_from_web(session):
    """从角色图鉴网页中提取角色名称（异步版）"""
    url = 'https://wiki.biligame.com/zzz/%E8%A7%92%E8%89%B2%E5%9B%BE%E9%89%B4'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Referer': 'https://wiki.biligame.com/zzz/'
    }
    
    try:
        print(f"正在从网页获取角色图鉴数据: {url}")
        async with session.get(url, headers=headers, timeout=30) as response:
            if response.status != 200:
                print(f"请求失败，状态码: {response.status}")
                return []
            
            text = await response.text(encoding='utf-8')
            soup = BeautifulSoup(text, 'html.parser')
            role_boxes = soup.select('#CardSelectTr .role-box')
            character_names = []
            
            for box in role_boxes:
                name_tag = box.select_one('.role-name a')
                if name_tag:
                    character_names.append(name_tag.get_text(strip=True))
            
            return character_names
    except Exception as e:
        print(f"从网页提取角色名称失败: {str(e)}")
        return []

async def fetch_character_detail(session, char_name, semaphore):
    """抓取单个角色的详细数据（异步版）"""
    # URL 编码角色名
    encoded_name = quote(char_name, safe='')
    url = f"https://wiki.biligame.com/zzz/{encoded_name}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Referer': 'https://wiki.biligame.com/zzz/'
    }
    
    async with semaphore:
        try:
            print(f"  正在抓取: {char_name}")
            async with session.get(url, headers=headers, timeout=30) as response:
                if response.status != 200:
                    print(f"  请求失败，状态码: {response.status}")
                    return None
                
                text = await response.text(encoding='utf-8')
                soup = BeautifulSoup(text, 'html.parser')
                
                # 提取角色基本信息
                character_info = {
                    'name': char_name,
                    'url': url,
                    'encoded_name': encoded_name,
                    'fetch_time': time.strftime('%Y-%m-%d %H:%M:%S')
                }
                
                # 1. 查找角色名称
                title = soup.find('h1', {'id': 'firstHeading'})
                if title:
                    character_info['title'] = title.get_text(strip=True)
                
                # 2. 查找角色信息表格
                info_table = soup.find('table', class_=['wikitable', 'infobox'])
                if info_table:
                    info_dict = {}
                    rows = info_table.find_all('tr')
                    for row in rows:
                        th = row.find('th')
                        td = row.find('td')
                        if th and td:
                            key = th.get_text(strip=True)
                            value = td.get_text(strip=True)
                            info_dict[key] = value
                            # 提取全名和英文名称
                            if '全名' in key or '本名' in key:
                                # 支持中文括号和英文括号
                                match = re.match(r'(.+?)\s*[（(](.+?)[）)]', value)
                                if match:
                                    character_info['full_name'] = match.group(1).strip()
                                    # 将英文名称中的空格替换为下划线
                                    character_info['english_name'] = match.group(2).strip().replace(' ', '_')
                                else:
                                    character_info['full_name'] = value.strip()
                                    character_info['english_name'] = None
                            # 提取属性/元素
                            if '属性' in key or '元素' in key or '元素属性' in key:
                                # 当td中包含img标签时，提取img之后的文本内容
                                if td.find('img'):
                                    # 获取img之后的所有文本内容
                                    element_text = ''
                                    for content in td.contents:
                                        # 跳过img标签
                                        if hasattr(content, 'name') and content.name == 'img':
                                            continue
                                        # 提取文本内容
                                        text_content = str(content).strip()
                                        if text_content:
                                            element_text += text_content
                                    character_info['element'] = element_text.strip()
                                else:
                                    character_info['element'] = value.strip()
                            # 提取稀有度/品级
                            if '稀有度' in key or '品级' in key:
                                # 稀有度通过图片的alt属性标识，如"角色稀有度S.png"
                                img_tag = td.find('img')
                                if img_tag:
                                    alt_text = img_tag.get('alt', '')
                                    # 从alt文本中提取稀有度等级（S/A/B/C）
                                    if '稀有度' in alt_text:
                                        # 查找稀有度等级字母
                                        match = re.search(r'稀有度([SABC])', alt_text)
                                        if match:
                                            character_info['rarity'] = match.group(1)
                                        else:
                                            # 如果没有匹配到，尝试从文件名中提取
                                            filename = alt_text.replace('.png', '')
                                            if 'S' in filename:
                                                character_info['rarity'] = 'S'
                                            elif 'A' in filename:
                                                character_info['rarity'] = 'A'
                                            elif 'B' in filename:
                                                character_info['rarity'] = 'B'
                                            elif 'C' in filename:
                                                character_info['rarity'] = 'C'
                                else:
                                    character_info['rarity'] = value.strip()
                            # 提取特性
                            if '特性' in key:
                                # 特性通过图片的alt属性标识，如"图标-强攻.png"
                                img_tag = td.find('img')
                                if img_tag:
                                    alt_text = img_tag.get('alt', '')
                                    # 从alt文本中提取特性名称（去掉"图标-"和".png"）
                                    if '图标-' in alt_text and '.png' in alt_text:
                                        character_info['trait'] = alt_text.replace('图标-', '').replace('.png', '')
                                    else:
                                        # 如果alt属性不符合预期格式，使用td中的文本
                                        character_info['trait'] = value.strip()
                                else:
                                    character_info['trait'] = value.strip()
                    character_info['basic_info'] = info_dict
                
                # 3. 提取立绘图片URL（官方介绍，非官方介绍2）
                character_info['stand_art_url'] = extract_stand_art_url(soup, char_name)
                
                print(f"  ✓ 成功抓取: {char_name}")
                return character_info
                
        except Exception as e:
            print(f"  ✗ 抓取角色 {char_name} 失败: {str(e)}")
            return None

def extract_stand_art_url(soup, char_name):
    """从HTML中提取立绘图片URL（纯立绘，排除官方介绍）"""
    try:
        # 查找所有包含"角色立绘"的图片
        images = soup.find_all('img', alt=re.compile(r'角色立绘'))
        
        for img in images:
            alt_text = img.get('alt', '')
            # 排除包含"官方介绍"的图片，只选择纯"角色立绘-XXX.png"
            if '角色立绘' in alt_text and '官方介绍' not in alt_text:
                img_url = img.get('src')
                if img_url:
                    print(f"  找到立绘图片: {alt_text}")
                    return img_url
        
        print(f"  未找到立绘图片（纯立绘）")
        return None
    except Exception as e:
        print(f"  提取立绘图片URL失败: {str(e)}")
        return None

async def download_stand_art(session, img_url, output_path, english_name):
    """下载立绘图片到指定路径（异步版）"""
    if not img_url:
        print(f"  图片URL为空，跳过下载")
        return False
    
    try:
        # 确保输出目录存在
        os.makedirs(output_path, exist_ok=True)
        
        # 构建文件名
        filename = f"{english_name}.png"
        filepath = os.path.join(output_path, filename)
        
        # 检查文件是否已存在
        if os.path.exists(filepath):
            print(f"  文件已存在，跳过下载: {filepath}")
            return True
        
        # 下载图片
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://wiki.biligame.com/zzz/'
        }
        
        print(f"  正在下载立绘图片: {img_url}")
        async with session.get(img_url, headers=headers, timeout=30) as response:
            if response.status != 200:
                print(f"  下载失败，状态码: {response.status}")
                return False
            
            # 保存图片
            with open(filepath, 'wb') as f:
                f.write(await response.read())
        
        print(f"  ✓ 立绘图片已保存: {filepath}")
        return True
        
    except Exception as e:
        print(f"  下载立绘图片失败: {str(e)}")
        return False

async def fetch_all_characters(session, character_names):
    """抓取所有角色的详细数据（异步版）"""
    # 创建信号量限制并发数
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
    
    print(f"开始抓取 {len(character_names)} 个角色的详细数据...")
    print("=" * 60)
    
    # 创建所有任务
    tasks = [fetch_character_detail(session, char_name, semaphore) for char_name in character_names]
    
    # 并发执行
    results = await asyncio.gather(*tasks)
    
    # 分离成功和失败的结果
    all_characters = [r for r in results if r is not None]
    failed_characters = [name for name, result in zip(character_names, results) if result is None]
    
    print("\n" + "=" * 60)
    print(f"抓取完成: 成功 {len(all_characters)} 个, 失败 {len(failed_characters)} 个")
    
    return {
        'fetch_time': time.strftime('%Y-%m-%d %H:%M:%S'),
        'total': len(character_names),
        'success': len(all_characters),
        'failed': len(failed_characters),
        'failed_list': failed_characters,
        'characters': all_characters
    }

def convert_format(data):
    """将数据转换为指定格式"""
    if not data:
        return None
    
    characters = data.get('characters', [])
    result = {
        "character": {}
    }
    
    for char in characters:
        # 获取英文名称作为键名
        english_name = char.get('english_name')
        if not english_name:
            # 如果没有英文名称，使用角色名作为键名
            english_name = char.get('name')
        
        # 构建角色数据
        char_data = {
            "CHS": char.get('full_name', char.get('name')),
            "EN": english_name,
            "code": english_name,
            "element": char.get('element', ''),
            "rarity": char.get('rarity', ''),
            "trait": char.get('trait', '')
        }
        
        # 添加到结果中
        result["character"][english_name] = char_data
    
    return result

def save_agent_yml(char_data, output_dir):
    """将单个角色数据保存为YAML文件（直接使用原始数据，不进行属性映射）"""
    # 获取数据（直接使用原始值）
    chs_name = char_data.get('CHS', '')
    code = char_data.get('code', '').lower()
    element = char_data.get('element', '')
    rarity = char_data.get('rarity', '')
    trait = char_data.get('trait', '')
    
    # 构建YAML内容（忽略weight，将特性填充到agent_type）
    yml_content = f"""agent_name: {chs_name}
agent_type: {trait}
dmg_type: {element}
rare_type: {rarity}
code: {code}
"""
    
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 构建文件名
    filename = f"{code}.yml"
    filepath = os.path.join(output_dir, filename)
    
    # 保存文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(yml_content)
    
    return filepath

def save_all_agent_yml(data, output_dir):
    """保存所有角色为单独的YAML文件"""
    if not data:
        return []
    
    saved_files = []
    characters = data.get('character', {})
    
    for code, char_data in characters.items():
        filepath = save_agent_yml(char_data, output_dir)
        saved_files.append(filepath)
        print(f"  已保存: {filepath}")
    
    return saved_files

def save_converted_data(data, filename='converted_character_data.json'):
    """保存转换后的数据"""
    if data:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(script_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"数据已保存到: {filepath}")
        return filepath

async def main():
    """主函数（异步版）"""
    print("=" * 60)
    print("角色数据抓取与格式转换工具（异步版）")
    print("=" * 60)
    
    # 创建异步HTTP会话
    async with aiohttp.ClientSession() as session:
        # 1. 从网页中提取角色名称
        print("\n从角色图鉴网页提取角色名称...")
        character_names = await extract_character_names_from_web(session)
        
        if not character_names:
            print("无法从网页提取角色名称")
            return
        
        print(f"\n从网页中提取到 {len(character_names)} 个角色名:")
        for i, name in enumerate(character_names[:10], 1):
            print(f"  {i}. {name}")
        if len(character_names) > 10:
            print(f"  ... 还有 {len(character_names) - 10} 个角色")
        
        # 2. 异步抓取所有角色的详细数据
        start_time = time.time()
        all_data = await fetch_all_characters(session, character_names)
        end_time = time.time()
        print(f"\n异步抓取耗时: {end_time - start_time:.2f} 秒")
        
        # 3. 转换格式
        print("\n转换数据格式...")
        converted_data = convert_format(all_data)
        
        if not converted_data:
            print("转换失败")
            return
        
        # 4. 保存数据
        output_path = save_converted_data(converted_data)
        
        # 5. 保存每个角色为单独的YAML文件
        print("\n" + "=" * 60)
        print("保存角色YAML文件")
        print("=" * 60)
        agent_output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'agent')
        saved_files = save_all_agent_yml(converted_data, agent_output_dir)
        print(f"\n✓ 已保存 {len(saved_files)} 个角色YAML文件到: {agent_output_dir}")
        
        # 6. 下载第一个角色的立绘图片
        print("\n" + "=" * 60)
        print("下载立绘图片")
        print("=" * 60)
        
        if all_data['characters']:
            first_char = all_data['characters'][0]
            english_name = first_char.get('english_name')
            stand_art_url = first_char.get('stand_art_url')
            
            if english_name and stand_art_url:
                print(f"\n下载第一个角色的立绘图片:")
                print(f"  角色名: {first_char.get('name')}")
                print(f"  英文名: {english_name}")
                print(f"  图片URL: {stand_art_url}")
                
                # 获取脚本所在目录
                script_dir = os.path.dirname(os.path.abspath(__file__))
                output_dir = os.path.join(script_dir, 'agent_stand_art')
                
                # 下载立绘图片
                success = await download_stand_art(session, stand_art_url, output_dir, english_name)
                
                if success:
                    print(f"\n✓ 立绘图片下载成功")
                else:
                    print(f"\n✗ 立绘图片下载失败")
            else:
                print(f"\n第一个角色没有立绘图片信息")
                print(f"  英文名: {english_name}")
                print(f"  图片URL: {stand_art_url}")
    
    # 6. 打印摘要
    print("\n" + "=" * 60)
    print("处理摘要")
    print("=" * 60)
    print(f"总角色数: {all_data['total']}")
    print(f"成功: {all_data['success']}")
    print(f"失败: {all_data['failed']}")
    print(f"转换角色数: {len(converted_data.get('character', {}))}")
    print(f"输出文件: {output_path}")

if __name__ == '__main__':
    # 运行异步主函数
    asyncio.run(main())
