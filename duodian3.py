import requests

import time
import json
import base64


class Vpn:
    def __init__(self, params):
        self.url = 'http://10.2.5.251:801/eportal/'
        self.user = params.get('user')
        self.pwd = params.get('pwd')
        self.type = params.get('type')
        self.type_list = ['', '@cmcc', '@unicom', '@telecom']

    def login(self):
        get_params = {
            'c': 'Portal',
            'a': 'login',
            'callback': 'dr' + str(int(time.time() * 1000)),
            'login_method': '1',
            'user_account': self.user + self.type_list[self.type],
            'user_password': self.pwd,
            'wlan_ac_ip': '',
            'wlan_ac_name': '',
            'jsVersion': '3.0',
            '_': str(int(time.time() * 1000)),
        }
        r = requests.get(self.url, params=get_params).text
        r = r.split('(')[1].split(')')[0]
        # print(r)
        r = json.loads(r)
        # print(r)

        # 建议测试登陆成功后，将下述代码注释
        ####################
        if r.get('result') == '1':
            print('登陆成功')
        else:
            msg = base64.b64decode(r.get('msg')).decode()
            if msg == 'userid error1':
                print('不存在此用户，请检查用户名是否填写错误，或者运行商选择错误')
            elif msg == 'userid error2':
                print('用户密码错误')
            elif msg:
                print('未知错误：', msg)
            else:
                print('无错误：', msg)
        ####################


if __name__ == '__main__':
    user_info = {
        'user': '12345678',  # 学号
        'pwd': '123456',  # 密码，默认身份证后六位
        'type': 2,  # 0,1,2,3分别对应校园网、移动、联通与电信。
    }
    vpn = Vpn(user_info)
    while True:
        vpn.login()
        time.sleep(5)  # 5秒循环检测
