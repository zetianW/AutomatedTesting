# 开发人员：泽天
import pytest


# 开发时间：2024/6/3 18:04

# 项目定义：
class Testapi:

    # 基础用法
    # @pytest.mark.parametrize('args', ['里斯', '王五', '赵六'])
    # def test_api1(self, args):
    #     print(args)

    # 相当于解包
    @pytest.mark.parametrize('name,age', [['里斯', 12], ['王五', 14], ['赵六', 19]])
    def test_api2(self, name, age):
        print(name, age)


if __name__ == '__main__':
    pytest.main(['w_test_api.py'])

