#-*- coding: utf-8 -*-
#@File    : baseApi.PY
#@Time    : 2022/7/9  17:19
#@Author  : haiyan
#@Email   : goodhaer@163.com
#@Software: PyCharm

import inspect
import os
from utils.handle_yaml import get_yaml_data
from configs.config_test import test_path,HOST
import requests
import  json
'''
思路:  token
order 业务
  yaml  写  接口url

公共基类：
    token

'''


class BaseApi:
    def __init__(self,intoken=None):


        self.data = get_yaml_data(os.path.join(test_path,'order.yaml'))[self.__class__.__name__]  # 类名下的token值
        # print(self.data)

        #

        self.content = intoken     #token  大多数业务会有 放在基类中





    def request_send(self,content1='',data=None,json=None,params=None):
        try:
            methodName = inspect.stack()[1][3]   # 谁调用我的request_send 方法 作为methodname
            path,method =self.data[methodName].values()


            if self.content :  #token 有值
                resp = requests.request(method=method,url=f'{HOST}{path}' + str(self.content), data=data, json=json,
                                        params=params)  # url = ...+token
            else:  #token没值
                resp = requests.request(method=method, url=f'{HOST}{path}' + str(content1), data=data, json=json,
                                        params=params)  #url = ... + ‘’
            return resp.json()
        except Exception as error:
            print(error)






    def createOrder(self,inData):
        result = self.request_send(data=inData)
        return result


    def payorder(self, inData, url):

        result = self.request_send(url,params=inData)
        return result

    def payedorder(self, inData):
        inData = json.dumps(inData)
        result = self.request_send(data=inData)
        return result




