import pytest
import allure
from utils.handle_yaml import get_yaml_caseData,test_path
from lib.Login import Logining
from commons.baseApi import ApiAssert
import os

@allure.feature('登录操作')
class TestLogin():
    @pytest.mark.parametrize('title,inbdoy,expData',get_yaml_caseData(os.path.join(test_path,'logincase.yaml')))
    def test_login(self,title,inbdoy,expData):
        res = Logining().login(inbdoy)
        print(res,'响应信息')
        print(expData,'响应信息2')
        ApiAssert.define_api_assert(expData['msg'], '=',res['msg'])



if __name__ == '__main__':
    pytest.main(['-s','test_login.py'])