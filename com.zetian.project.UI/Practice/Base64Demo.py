# 开发人员：泽天

# 开发时间：2024/1/16 18:52

# 项目定义：
import base64


def base_jm(args):
    str_zd = str(args).encode("utf-8")
    base_jmzd = base64.b64encode(str_zd).decode(encoding="utf-8")
    return base_jmzd


if __name__ == '__main__':
    print(base_jm("password"))
