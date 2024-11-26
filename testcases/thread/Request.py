# 开发人员：泽天

# 开发时间：2023/11/14 17:03

# 项目定义：
import json

import pytest
import requests


def post_glucose():
    # 请求地址
    # req_url = 'https://api.bokhealth.com/health-center/vital-callback/daily'
    req_url = 'https://bok-test.huadongmedia.com/health-center/vital-callback/daily'
    # headers
    headers = {
        'Content-Type': 'application/json',
        # 测试环境token
          'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJVc2VyIiwiZXhwIjozMjgxODI0NDkxLCJ1c2VySWQiOiItMTAxMCIsImlhdCI6MTcwNTAyNDQ5MX0.x9PAZccWt-Ky6yIMmCJi0OxDOJoWum7w2Za8kHiuJ6E'
        # 线上token
        # 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJVc2VyIiwiZXhwIjozMjgyODYyNDY2LCJ1c2VySWQiOiItMTAxMCIsImlhdCI6MTcwNjA2MjQ2Nn0.-H4jr2pfSULrFRrfcp6yHUfKYtAgrRO0tkKxsdBt4lk'
    }
    # 请求体
    data = {
        "data": {
            "data": [
                {

                    "timestamp": "2024-09-09T13:44:10",
                    "timezone_offset": "null",
                    "type": "automatic",
                    "unit": "mmol/L",
                    "value":4.4
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
            # "user_id": "f5d8f85f-42ce-440a-bc4e-acd1fc7cc8cb"  # xinzhaoguo2022@gmail.com     123456gzx测试环境账号d
            # "user_id": "2907071d-3af5-471e-b17e-929dec5c9461"  # zhengkun.zhang@huadongmedia.com 1111111111线上账号
            "user_id": "76eefc4e-b05c-11ee-ac51-26d6fed8a9ef"  # zetian.wang@huadongmedia.com  1111111111线上账号
            # "user_id": "c60d64a8-dba1-4349-95be-29ae2678e0b3"  # 18535106062@163.com           Zs931124. 测试环境账号
            # "user_id": "a8b1b107-3780-4985-8d83-8b6054c470ba"  # 张杰
        },
        "event_type": "daily.data.glucose.created"
    }
    # 发送请求并获取返回结果
    response_data = requests.post(url=req_url, headers=headers, data=json.dumps(data)).json()
    print(response_data)


print(post_glucose())
