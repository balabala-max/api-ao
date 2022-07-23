import sys
import pytest
from lib.Login import Logining
from configs.config_test import RQS
from utils.handle_yaml import ordercase
from lib.Loginpuls import Order
from utils.bianliang import clear_yaml


# 在所有的接口请求之前执行清空文件里的内容
@pytest.fixture(scope="session",autouse=True)
def clear_token():
    print('接口之前请理文件内容')
    clear_yaml()



#-------登录操作--------
@pytest.fixture(scope='session')
def login_init():
    print('用户登录操作')
    _token  = Logining().login(RQS,getToken=True)
    yield  _token
    print('登录完成')


#--------创建接口实例-----------
@pytest.fixture(scope='class')
def order_init(login_init):
    print('------店铺实例开始-------')
    orderObject = Order(login_init)

    yield orderObject
    print('结束')


@pytest.fixture(scope='class')
def order_init1():
    print('------订单实例开始-------')
    orderObject1 = Order()

    yield orderObject1
    print('结束')

#------------yaml封装--------------、
@pytest.fixture(scope='function')
def test_data(request):
    test_name = request.function.__name__
    # print('信息信息在这',test_name)
    return  ordercase.get(test_name)