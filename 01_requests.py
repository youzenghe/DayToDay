import requests
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"
}
url = "https://fanyi.baidu.com/sug"
data = {
    "kw":"怎么样"
}
response = requests.post(url, headers=headers, data=data).json()
print(response)