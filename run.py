# 开发人员：泽天
# import os
#
# import pytest
#
# # 开发时间：2024/4/1 16:24
#
# # 项目定义：
# if __name__ == '__main__':
#     pytest.main()
#     os.system("allure generate ./reports -o ./reports/temp --clean")
#  #   os.system("allure generate ./reports/assets -o ./reports/temp --clean")
import os
import pytest

if __name__ == '__main__':
    pytest.main(["-vs", "--alluredir=./reports/temp"])
    os.system("allure generate ./reports/temp -o ./reports/html --clean")

