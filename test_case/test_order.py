import pytest
import allure
import jsonpath
from utils.handle_yaml import replace_yaml
from utils.bianliang import write_yaml,read_yaml1,read_yaml
from configs.config_test import HOST
from utils.handle_yaml import replace_yaml
from string import Template
import string
import  jinja2
import json
import os
report_path = '../report/tmp'
@allure.epic('小程序订单项目')
class TestOrder:

    # @pytest.mark.testorder
    @allure.story('小程序订单流程')
    # @pytest.mark.parametrize('title,inBody,expData',get_yaml_caseData(orderyaml,'test_login'))
    def test_order_case(self,test_data,order_init,login_init):
        with allure.step('1--用户登录 + 创建订单'):
            print(test_data)
            #createOrder 不能直接调用，只能再conftest 创建实例md

            res = test_data['data']   #请求参数
            resp = order_init.createOrder(res)  #test_data['data] 是请求参数
            print('响应值',resp)

            #提取orderno 订单号  把返回值 订单号存储到 到变量yaml里
            orderno = jsonpath.jsonpath(resp,"$.orderno")[0]
            os.environ["orderno"] = orderno
            #将orderno 写再bianliang 文件里
            write_yaml({"orderno":orderno})
            write_yaml({"token":login_init})

            print('信息信息',test_data['expdata']['msg'])
            assert resp['code'] ==  test_data['expdata']['code']

    @allure.story('小程序订单流程')
    def test_pay_order_1(self,test_data,order_init1,login_init):
        with allure.step('2--调用支付接口'):

            orderno = read_yaml1()['orderno']
            print('订单号',orderno)
            #对token 替换
            template = string.Template(login_init)  # token值
            test_data['data']['token'] = template.safe_substitute(test_data['data']['token'])


            orderpath = str(read_yaml()['Order']['payorder']['path']).format(orderno)  # 字符串形式


            print('替换token',test_data['data'])
            print('替换path',orderpath)
            #
            # print('替换后的结果',test_data['data'])
            resp = order_init1.payorder(test_data['data'],url=orderno)
            print('支付接口响应值',resp)

            assert resp['code'] == test_data['expdata']['code']

    @allure.story('小程序订单流程')
    def test_payorder(self,test_data,order_init1):
        with allure.step('3-支付成功'):
            orderno = read_yaml1()['orderno']
            template2 = string.Template(orderno)  # token值
            test_data['data']['orderno'] = template2.safe_substitute(test_data['data']['orderno'])
            print('data信息',test_data['data'])
            resp = order_init1.payedorder(test_data['data'])
            assert resp['code'] == test_data['expdata']['code']











if __name__ == '__main__':
    pytest.main(['test_order.py', '-s', '--alluredir', f'{report_path}', '--clean-alluredir'])
    os.system(f'allure serve {report_path}')








