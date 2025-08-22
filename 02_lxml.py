import requests
from lxml import etree
import json
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"
}
n = input()
url = "https://baike.baidu.com/item/"+f"{n}"
response = requests.get(url, headers=headers)
data = response.content.decode()
html = etree.HTML(data)
List = html.xpath('//meta[@name="description"]/@content')
Dict = {
    n:List[0]
}
with open("./ren.json","a",encoding="utf-8") as f:
    json.dump(Dict, f, ensure_ascii=False, indent=2)