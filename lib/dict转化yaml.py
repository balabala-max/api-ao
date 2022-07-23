#-*- coding: utf-8 -*-
#@File    : 11.PY
#@Time    : 2022/7/17  11:51
#@Author  : haiyan
#@Email   : goodhaer@163.com
#@Software: PyCharm


import yaml


def save_dict_to_yaml(dict_value: dict, save_path: str):
    """dict保存为yaml"""
    with open(save_path, 'a') as file:
        file.write('\r\n')
        file.write(yaml.dump(dict_value, allow_unicode=True))


def read_yaml_to_dict(yaml_path: str, ):
    with open(yaml_path) as file:
        dict_value = yaml.load(file.read(), Loader=yaml.FullLoader)
        return dict_value


if __name__ == '__main__':
    my_config_dict =[{
		'detail':'登录接口',
		'data': {
        "openid": "1234",
        "appid": "4567",
        "unionid": "23231442"
    },
		'expdata':{
					"mdg": "登录成功!",
					"code": 0,
					"token":"234af73571da46ade79ea6a74961b1d23d609b79"
}
	}]
    # 保存yaml
    save_dict_to_yaml(my_config_dict, "config.yaml")
    # 读取yaml
    config_value = read_yaml_to_dict("config.yaml")
    # assert config_value == my_config_dict
