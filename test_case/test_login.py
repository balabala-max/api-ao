import pytest
import allure
from utils.handle_yaml import get_yaml_caseData,test_path
from lib.Login import Logining
from commons.baseApi import ApiAssert
from configs.logger import logger
import os
report_path = '../report/tmp'
@allure.epic('小程序订单项目')
@allure.feature('登录操作')
class TestLogin():
    @pytest.mark.parametrize('title,inbdoy,expData',get_yaml_caseData(os.path.join(test_path,'logincase.yaml')))
    def test_login(self,title,inbdoy,expData):
        res = Logining().login(inbdoy)
        logger.info('登录请求参数{}'.format(inbdoy))
        logger.info(('登录响应参数{}'.format(res)))
        ApiAssert.define_api_assert(expData['msg'], '=',res['msg'])



if __name__ == '__main__':
    pytest.main([ '-q','-s','test_login.py'])

