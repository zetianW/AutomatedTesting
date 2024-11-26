# 开发人员：泽天
import os

import yaml

# 开发时间：2024/6/4 10:45

# 项目定义：读取yaml文件
import os
# import yaml


def read_testcase_yaml(yaml_util):
    yaml_path = os.path.join(os.getcwd(), "testApi", yaml_util)

    try:
        with open(yaml_path, mode='r', encoding='utf-8') as f:
            # 显式指定 Loader 参数以增强安全性
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value
    except FileNotFoundError:
        print(f"文件未找到: {yaml_path}")
        return None
    except yaml.YAMLError as exc:
        print(f"YAML解析错误: {exc}")
        return None
    except Exception as e:
        print(f"读取文件时发生未知错误: {e}")
        return None

