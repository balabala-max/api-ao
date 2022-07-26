#-*- coding: utf-8 -*-
#@File    : handle_yaml.PY
#@Time    : 2022/7/9  21:18
#@Author  : haiyan
#@Email   : goodhaer@163.com
#@Software: PyCharm


import yaml,os,json
from configs.config_test import test_path

'''
思路; 
解析yaml文件
    1--写一个方法  get_yaml_data   （方便在执行用例时候能解析yaml数据）
    2--文件在磁盘，用open函数打开，在内存中打开
        返回yaml  
    
'''

def get_yaml_data(fileDir):

    with open(fileDir,encoding='utf-8') as e:
        result =   yaml.safe_load(e.read())
        return result


#获取yaml 数据放到元组内，好方便pytest 拿到函数检索
def  get_yaml_caseData(firDir,yongliname):
    resList = []
    res = get_yaml_data(firDir)
    resList.append((res[yongliname]['detail'],
                    res[yongliname]['data'],
                    res[yongliname]['expdata']))
    return resList



orderyaml = os.path.join(test_path,'tt.yaml')
mysqlyaml = os.path.join(test_path,'mysql_data.yaml')

ordercase = get_yaml_data(orderyaml)
mysql_yamldata = get_yaml_data(mysqlyaml)
print(mysql_yamldata['init_sql']['select_user'])
mysql_select  = str(mysql_yamldata['init_sql']['select_user'])
