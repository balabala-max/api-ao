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

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
test_path = os.path.join(project_path,'data')


