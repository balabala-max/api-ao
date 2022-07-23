#-*- coding: utf-8 -*-
#@File    : Login.PY
#@Time    : 2022/7/10  12:51
#@Author  : haiyan
#@Email   : goodhaer@163.com
#@Software: PyCharm

from commons.baseApi import BaseApi
import os
class Logining(BaseApi):
    # def login(self,inData):
    #     url = f'{HOST}/api/v1/member-auth/wechat-member/idomall/is-exist-user'
    #
    #
    #     resp = self.request_send(params=inData)
    #     return resp.json()
    def login(self,inData,getToken=False):
        resp = self.request_send(params=inData)
        if getToken:
            return resp['token']
        else:
            return resp








if __name__ == '__main__':
    rqs = {
        "openid": "1234",
        "appid": "4567",
        "unionid": "23231442"
    }
    # rqs = json.dumps(rqs)

   #将类实例化
    a = Logining().login(rqs,getToken=True)   # 调取baseApi 中的login

