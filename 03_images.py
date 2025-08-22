import requests
from lxml import etree
from selenium import webdriver
n = input("输入要爬取谁的图片：\n")
driver = webdriver.Chrome()
headers = {
 "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}
proxies = {
    "http":"127.0.0.1:7890",
    "https":"127.0.0.1:7890"
}
url = "https://baike.baidu.com/item/"+f"{n}"
driver.get(url)
data = driver.page_source
html = etree.HTML(data)
newdata = html.xpath('//div[@class="abstractAlbum_CSG3E"]/img/@src')
lj = newdata[0]
response = requests.get(lj, headers=headers, proxies=proxies)
with open(f"{n}.jpg", "wb") as f:
    f.write(response.content)
driver.quit()