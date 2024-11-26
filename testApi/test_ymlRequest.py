# 开发人员：泽天
import pytest
import requests

# 开发时间：2024/6/4 10:14

# 项目定义：
# 开发人员：泽天

# 开发时间：2024/3/1 17:21

# 项目定义：
import yaml_util
import pytest


class TestYmlRequest:

    @pytest.mark.parametrize('caseinfo',
                             yaml_util.read_testcase_yaml('/Users/edy/PycharmProjects/conftest_httpRunner/Demo/extract.yml'))
    def test_set_glucose(self, caseinfo):
        print(caseinfo['name'])
        req_url = caseinfo['request']['url']
        headers = caseinfo['request']['headers']
        data = caseinfo['request']['data']

        # 发送请求并获取返回结果
        response = requests.post(url=req_url, headers=headers, json=data).json()
        print(response)
