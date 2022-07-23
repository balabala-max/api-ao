# 小程序订单    分为门店订单  和  非门店订单

'''
注意： param：get   data： post
'''
from configs.config_test import HOST
from commons.baseApi import BaseApi
from lib.Login import Logining
import requests
import json
from commons.goloaldata import GlobalData
from utils.bianliang import read_yaml

class Order(BaseApi):

    def createOrder(self,inData):
        if isinstance(inData,dict)==True:
            inData = json.dumps(inData)
            resp=self.request_send(data=inData)
        return resp

    # def payorder(self, inData, url):
    #
    #     result = self.request_send(url,data=inData)
    #     return super(Order,self).payorder(inData,url)



if __name__ == '__main__':

    rqs = {
        "openid": "1234",
        "appid": "4567",
        "unionid": "23231442"
    }
    # _token = Logining().login(rqs,getToken=True)
    # order = Order(_token)
    #
    inData = {
    "address": 223,
    "channel": "2",
    "channelShopCode": "M2-1001",
    "code": "",
    "internalPurchaseVo": [
        {
            "brandNo": 10,
            "count": 1,
            "goodsName": "BOOM",
            "salesPrice": 1999,
            "sku": "200502667",
            "spu": "P00211",
            "saleType": 2,
            "offlineStoreCode": "1166",
            "guideInfo": "",
            "activityId": ""
        }
		]}
    #创建订单
    _token = Logining().login(rqs,getToken=True)
    order1 = Order(_token)
    creaorder = order1.createOrder(inData)
    print('创建订单',creaorder)
    orderno = creaorder['orderno']
    print(type(orderno))
    print(orderno)
    print(type(orderno))

    GlobalData().cookie['orderno'] = orderno
    data = GlobalData().cookie['orderno']



    doct = read_yaml()['Order']['payorder']['path']
    print('zifuc',doct)
    print(str(doct))
    print(type(doct))
    a = "/perfume/order/wxpay/mp2/{}".format("123213213213213")
    # print(a)

    b = read_yaml()['Order']['payorder']['path'].format(data)
    print('替换path',b)
    print(type(b))
    # 调支付接口
    res = {
        "token": _token,
        "openid": rqs["openid"],
        "store":1020
    }

    # 调支付接口
    # 调支付接口
    order = Order()  # 创建实例
    payord = order.payorder(res,orderno)
    print('调支付接口成功》》》》》',payord)
    #
    #
    #支付成功
    res2 = {
            "orderprice":"32145",
            "orderno":creaorder
            }
    print(res2)
    #

    print(order.payedorder(res2))




