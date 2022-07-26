import os
HOST =  'http://127.0.0.1:5555'

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

MYSQL_HOST = "192.168.7.125"
MYSQL_PORT = 3306
MYSQL_USER = "o2ouser"
MYSQL_PASSWD = "ydprzuo2&5fdKG2i"
MYSQL_DB = "pay_dev2"



project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
test_path = os.path.join(project_path,'data')


