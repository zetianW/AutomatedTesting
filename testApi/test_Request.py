# 开发人员：泽天

# 开发时间：2024/3/1 17:21

# 项目定义：
import json

import pytest
import requests


class TestRequest:

    # @pytest.mark.smoke   标记改方法是冒烟测试用例
    #  @pytest.mark.manager

    def test_post_glucose(self, conn_database):
        # 请求地址
        req_url = 'https://bok-test.huadongmedia.com/health-center/vital-callback/daily'
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
                        "timestamp": "2024-04-22T13:37:00",
                        "timezone_offset": "null",
                        "type": "automatic",
                        "unit": "mmol/L",
                        "value": 6.6
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
                "user_id": "c60d64a8-dba1-4349-95be-29ae2678e0b3"
            },
            "event_type": "daily.data.glucose.created"
        }
        # 发送请求并获取返回结果///json.dumps(data)序列化///json.loads(data)反序列化
        response_data = requests.post(url=req_url, headers=headers, data=json.dumps(data)).json()
        print(response_data)
