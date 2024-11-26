# 开发人员：泽天
import unittest


# 开发时间：2024/6/4 15:55

# 项目定义：
class TestEasyDemo(unittest.TestCase):
    def test_outprint01(self):
        print("hello")

    def test_outprint02(self):
        print("world")


if __name__ == '__main__':
    TestEasyDemo()
