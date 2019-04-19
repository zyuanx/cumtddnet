# coding utf-8
import urllib2
import time
import json


class Vpn:
    def __init__(self, params):
        self.url = {
            'urlLogin': 'http://10.2.5.251:801/eportal/?c=Portal&a=login&callback=dr'+str(int(time.time()*1000))+'&login_method=1&user_account='+params['user']+'&user_password='+params['pwd']+'&wlan_ac_ip=&wlan_ac_name=NAS&jsVersion=3.0&_='+str(int(time.time()*1000)),
        }

    def login(self):
        r = urllib2.Request(self.url['urlLogin'])
        res = urllib2.urlopen(r, timeout=20).read()
        return json.dumps(res)


if __name__ == '__main__':
    user_account = {
        'user': '00000000',
        'pwd': '000000'
    }
    vpn = Vpn(user_account)
    while True:
        result = vpn.login()
        time.sleep(5)
        print result
# ---------------------------by: Zhiyuan Li