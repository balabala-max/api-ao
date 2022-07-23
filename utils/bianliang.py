from string import Template
import yaml
import requests
import pytest

def read_yaml():
    with open("../data/order.yaml",encoding='utf-8') as e:
        result =   yaml.safe_load(e.read())
        return result

def read_yaml1():
    with open("../data/downdata.yaml", encoding="utf-8")as f:
        value = yaml.load(f,Loader=yaml.FullLoader)
        return value

# 写入
def write_yaml(data):
    with open("../data/downdata.yaml",encoding="utf-8",mode="a")as f:
        value = yaml.dump(data,stream=f,allow_unicode=True)

# 清空
def clear_yaml():
    with open('../data/downdata.yaml', mode='w', encoding='utf-8') as f:
        f.truncate()

