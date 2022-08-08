import yaml
import os
from configs.config_test import test_path


def read_yaml():
    with open(os.path.join(test_path,'order.yaml'),encoding='utf-8') as e:
        result =   yaml.safe_load(e.read())
        return result

def read_yaml1():
    with open(os.path.join(test_path,'downdata.yaml'), encoding="utf-8")as f:
        value = yaml.load(f,Loader=yaml.FullLoader)
        return value

# 写入
def write_yaml(data):
    with open(os.path.join(test_path,'downdata.yaml'),encoding="utf-8",mode="a")as f:
        value = yaml.dump(data,stream=f,allow_unicode=True)

# 清空
def clear_yaml():
    with open(os.path.join(test_path,'downdata.yaml'), mode='w', encoding='utf-8') as f:
        f.truncate()

