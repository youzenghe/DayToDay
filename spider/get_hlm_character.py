from urllib import request
from urllib.parse import quote
import string
import time
import json
from bs4 import BeautifulSoup
import codecs
import os

# 请确保你有 get_character_array.py 文件，并有 get_character() 方法
from get_character_array import get_character

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def get_json(character_arr):
    img_dir = ensure_dir(os.path.abspath("../spider/images"))
    json_dir = ensure_dir(os.path.abspath("../json"))

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }

    data = {}

    for i in set(character_arr):
        print(f"正在处理：{i}")
        url = r'https://baike.baidu.com/item/' + i
        url = quote(url, safe=string.printable)
        req = request.Request(url, headers=headers)
        try:
            response = request.urlopen(req, timeout=20)
            html = response.read().decode('utf-8')
        except Exception as e:
            print(f"请求失败: {i}, 错误: {e}")
            continue

        soup = BeautifulSoup(html, 'html.parser')

        # 图片提取逻辑，优先主图区块
        img_tag = None
        # 1. 优先找 summary-pic 区块
        res = soup.find(class_="summary-pic")
        if res:
            img_tag = res.find('img')
        # 2. 如果没找到，再找 lemmaWgt-pic
        if not img_tag:
            res2 = soup.find(class_="lemmaWgt-pic")
            if res2:
                img_tag = res2.find('img')
        # 3. 如果还没找到，再找第一个图片，但过滤默认图片
        if not img_tag:
            img_tags = soup.find_all('img')
            for t in img_tags:
                img_src = t.get('src', '')
                img_alt = t.get('alt', '')
                # 过滤默认图片
                if '暂无图片' in img_alt or '百科' in img_alt or 'none' in img_src:
                    continue
                img_tag = t
                break

        if img_tag and img_tag.get('src'):
            img_src = img_tag.get('src')
            img_alt = img_tag.get('alt', '')
            # 过滤默认图片、无效图片
            if '暂无图片' in img_alt or '百科' in img_alt or 'none' in img_src:
                print(f"{i} 是默认图片，跳过图片下载")
            else:
                if img_src.startswith('//'):
                    img_src = 'https:' + img_src
                elif img_src.startswith('/'):
                    img_src = 'https://baike.baidu.com' + img_src
                pic_name = os.path.join(img_dir, str(i) + '.jpg')
                try:
                    request.urlretrieve(img_src, pic_name)
                    print(f"图片已保存: {pic_name}")
                except Exception as e:
                    print(f"下载图片失败: {i}, 错误: {e}")
        else:
            print(f"{i} 找不到主图或为默认图片")

        # 信息提取
        res_key = soup.find_all(class_="basicInfo-item name")
        res_val = soup.find_all(class_="basicInfo-item value")
        key = [ik.get_text().strip().replace("\n", "、") for ik in res_key]
        value = [iv.get_text().strip().replace("\n", "、") for iv in res_val]
        item = dict(zip(key, value))
        data[str(i)] = item

        # 防止请求太快被封
        time.sleep(1)

    # 保存为JSON
    json_path = os.path.join(json_dir, 'data.json')
    with codecs.open(json_path, 'w', 'utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2))
    print(f"数据已保存: {json_path}")

if __name__ == "__main__":
    character_arr = get_character()
    get_json(character_arr)