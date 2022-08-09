import pytest
import allure
import jsonpath
import logging
import json
from commons.mysql_operate import db
from configs.logger import logger
from utils.bianliang import write_yaml,read_yaml1,read_yaml
from utils.handle_yaml import mysql_yamldata
from commons.baseApi import ApiAssert
from string import Template
import string

import os
report_path = '../report/tmp'
@allure.epic('小程序订单项目')
class TestOrder:

    # @pytest.mark.testorder
    logger.info("----------------------------测试开始-----------------------------")
    @allure.title('1--用户登录 + 创建订单')
    @allure.story('小程序订单流程')
    def test_order_case(self,test_data,order_init,login_init):
        with allure.step('1--用户登录 + 创建订单'):

            #createOrder 不能直接调用，只能再conftest 创建实例md

            res = test_data['data']   #请求参数
            logger.info('创建订单请求参数：{}'.format(res))
            resp = order_init.createOrder(res)  #test_data['data] 是请求参数

            logger.info('1-创建订单响应值：{}'.format(resp))


            #提取orderno 订单号  把返回值 订单号存储到 到变量yaml里
            orderno = jsonpath.jsonpath(resp,"$.orderno")[0]
            os.environ["orderno"] = orderno
            #将orderno 写再bianliang 文件里
            write_yaml({"orderno":orderno})
            write_yaml({"token":login_init})

            print('信息信息',test_data['expdata']['msg'])
            logger.info('实际结果：{}， 期望结果{}'.format(resp, test_data['expdata']))
            ApiAssert.define_api_assert(resp['code'],'=',test_data['expdata']['code'])

    @allure.title('2--调用支付接口')
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
            logger.info('2调用支付接口---请求参数======》{}'.format(test_data['data']))
            resp = order_init1.payorder(test_data['data'],url=orderno)
            # print('支付接口响应值',resp)
            logging.info('支付接口响应值=======>{}'.format(resp))

            logger.info('实际结果：{}， 期望结果{}'.format(resp, test_data['expdata']))
            ApiAssert.define_api_assert(resp['code'],'=',test_data['expdata']['code'])

    @allure.title('3-支付接口')
    @allure.story('小程序订单流程')
    def test_payorder(self,test_data,order_init1):
        with allure.step('3-支付接口'):
            orderno = read_yaml1()['orderno']
            #数据库  查找 item_ibz_id
            mysql_select = str(mysql_yamldata['init_sql']['select_user'][0])

            msqlselect_list = mysql_select.format(orderno)
            logger.info('小程序sql语句{}'.format(msqlselect_list))
            # msqlselect_list = list(eval(msqlselect_list))
            logging.info("sql语句=======》",mysql_select)
            data = db.select_db(msqlselect_list)
            print(data,'data信息公开')
            print('mysql  item_biz_id信息',data[0]['item_biz_id'])
            logger.info('取item_biz_id信息：{}'.format(data[0]['item_biz_id']))
            itemibzid = data[0]['item_biz_id']
            write_yaml({"item_biz_id":itemibzid})

            # 查找价格
            mysql_data = str(mysql_yamldata['init_sql']['select_user'][1])
            msqlselect_price = mysql_data.format(itemibzid)




            order_price = db.select_db(msqlselect_price)
            orderprice = order_price[0]['amount']
            logger.info('取价格信息{}'.format(orderprice))
            write_yaml({"orderprice":orderprice})


            #替换
            test_data['data'] = Template(json.dumps(test_data['data'])).safe_substitute(itemibzid=itemibzid,orderprice=orderprice)  # item_biz_id值

            print('oooo',test_data['data'])


            res = test_data['data']
            res = json.loads(res)   #转字典形式
            logger.info('调用接口请求参数:{}'.format(res))
            resp = order_init1.payedorder(res)
            logger.info('调用接口响应值值：{}'.format(resp))

            logger.info('实际结果：{}， 期望结果{}'.format(resp,test_data['expdata']))
            ApiAssert.define_api_assert(resp['code'],'=',test_data['expdata']['code'])

            logger.debug("-------------------------------测试结束--------------------------------------")









if __name__ == '__main__':
    pytest.main(['-q', '-s', 'test_order.py'])
    # pytest.main(['test_order.py', '-s', '--alluredir', f'{report_path}', '--clean-alluredir'])
    # os.system(f'allure serve {report_path}')








