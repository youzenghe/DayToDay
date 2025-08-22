import requests
import json

class JinShan:
    def __init__(self):
        self.proxies = {
            'http': 'http://127.0.0.1:7890',
            'https': 'http://127.0.0.1:7890',
        }
        self.data = {
         "kw":"你好"
        }

        self.url = 'https://fanyi.baidu.com/sug'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"
        }

    def get_json(self):
        response = requests.post(
            self.url,
            headers=self.headers,
            data=self.data
        )
        return response.json()

    def run(self):
        print(self.get_json()["data"][1])


if __name__ == '__main__':
    js = JinShan()
    js.run()
