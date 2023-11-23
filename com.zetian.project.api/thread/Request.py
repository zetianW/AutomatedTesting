# 开发人员：泽天

# 开发时间：2023/11/14 17:03

# 项目定义：
import json
import requests


def huaDong():
    # 请求地址
    req_url = 'https://online-office-api-test.huadongmedia.com/open/api/add/user'
    # headers
    headers = {
        'Content-Type': 'application/json',
        'Signature': 'shanyi_07e80d50c3304090a71b2e171778676e_0c8e0a1f8a4081afd179200ff24b215d'
    }
    # 请求体
    data = {
        "nickName": "Alex",
        "headPortrait": "https://nebulos-img.huadongmeta.com/nebulos/img/gridView.a41882a1.png",
        "post": "test",
        "unit": "花动",
        "selfEditable": "true"
    }
    # 发送请求并获取返回结果
    response_data = requests.post(url=req_url, headers=headers, data=json.dumps(data)).json()
    print(response_data)


print(huaDong())
