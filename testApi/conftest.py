# 开发人员：泽天
import pytest


# 开发时间：2024/4/22 17:33

# 项目定义：
@pytest.fixture(scope="function")
def conn_database():
    print("start")
    yield
    print("end")

# 配合yaml使用，这儿只是个例子
# @pytest.fixture(scope="session", autouse=True)
# def p_out():
#     print("每次都会重新请求")
