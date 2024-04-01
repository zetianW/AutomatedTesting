# 开发人员：泽天

# 开发时间：2024/3/1 17:21

# 项目定义：
import json

import pytest
import requests


class TestRequest:

    def test_post_glucose(self):
        # 请求地址
        req_url = 'http://bok-test.huadongmedia.com/health-center/vital-callback/daily'
        # headers
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJVc2VyIiwiZXhwIjozMjgxODI0NDkxLCJ1c2VySWQiOiItMTAxMCIsImlhdCI6MTcwNTAyNDQ5MX0.x9PAZccWt-Ky6yIMmCJi0OxDOJoWum7w2Za8kHiuJ6E'
        }
        # 请求体
        data = {
            "data": {
                "data": [
                    {

                        "timestamp": "2024-03-01T01:30:00",
                        "timezone_offset": "null",
                        "type": "automatic",
                        "unit": "mmol/L",
                        "value": 5.7
                    }
                ],
                "provider": {
                    "logo": "https://storage.googleapis.com/vital-assets/freestyle.png",
                    "name": "Freestyle Libre",
                    "slug": "freestyle_libre"
                },
                "source": {
                    "logo": "https://storage.googleapis.com/vital-assets/freestyle.png",
                    "name": "Freestyle Libre",
                    "slug": "freestyle_libre"
                },
                "source_id": 10,
                "user_id": "0dc126ed-5b1d-4ee2-bc0e-183cd1a614da"
            },
            "event_type": "daily.data.glucose.created"
        }
        # 发送请求并获取返回结果///json.dumps(data)序列化///json.loads(data)反序列化
        response_data = requests.post(url=req_url, headers=headers, data=json.dumps(data)).json()
        print(response_data)


if __name__ == '__main__':
    pytest.main()

