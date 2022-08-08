import os
HOST =  'http://8.142.81.77:5555'

RQS = {
        "openid": "1234",
        "appid": "4567",
        "unionid": "23231442"
    }

jiangRqs = {
			"openid": "1234",
			"appid": "4567",
			"unionid": "23231442"
		}

MYSQL_HOST = "8.142.81.77"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PASSWD = "jiang.123"
MYSQL_DB = "pay_dev2"



project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
test_path = os.path.join(project_path,'data')


