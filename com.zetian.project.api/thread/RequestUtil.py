# 开发人员：泽天

# 开发时间：2024/4/1 14:26

# 项目定义：
import requests


class RequestUtil:
    sess = requests.Session()

    def all_send_request(self, **kwargs):
        res = RequestUtil.sess.request(**kwargs)
        print(kwargs["method"])
        print(res.text)
        return res
