#!/usr/bin/python python3
# coding=utf-8
'''
Author: whalefall
Date: 2021-07-08 12:38:04
LastEditTime: 2021-07-09 03:00:56
Description: 句子控各接口测试
'''
import requests
import urllib3
import time
urllib3.disable_warnings()


class CheckPhone(object):
    '''
    检查验证手机号码类
    '''

    def __init__(self, mobile) -> None:
        self.mobile = mobile

    def send_code(self):
        '''
        发送手机验证码
        '''
        headers = {
            'Authorization': '',
            'User-Agent': 'axe/2.5.3 (build:2056;channel:huawei;Android6.0;EMUIEmotionUI_4.0.1)zh_CN',
            'n2c': 'axe',
            'n2v': '2.5.3',
            'n2p': 'android',
            'n2token': '',  # 登录才可获取
            'n2deviceId': '0866693028533631300003803900CN01',
            'n2uuid': '',
            'n2brand': 'HUAWEI',
            'n2model': 'HUAWEI GRA-TL00',
            'n2os': 'Android6.0',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'api.juzikong.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
        }

        data = {
            'timestamp': int(time.time()),  # 时间戳
            'mobile': self.mobile,  # 手机号码
            'sign': ''  # sign: 不传好像没啥事情
        }

        response = requests.post('https://api.juzikong.com/mobi/mg/services/sendVerifyCode',
                                 headers=headers, data=data, verify=False)
        print(response.text)

    def check_code(self):
        '''
        检查手机验证码
        '''
        headers = {
            'Authorization': '',
            'User-Agent': 'axe/2.5.3 (build:2056;channel:huawei;Android6.0;EMUIEmotionUI_4.0.1)zh_CN',
            'n2c': 'axe',
            'n2v': '2.5.3',
            'n2p': 'android',
            'n2token': '',
            'n2deviceId': '0866693028533631300003803900CN01',
            'n2uuid': '',
            'n2brand': 'HUAWEI',
            'n2model': 'HUAWEI GRA-TL00',
            'n2os': 'Android6.0',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'api.juzikong.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
        }

        data = {
            'timestamp': int(time.time()),  # 时间戳
            'mobile': self.mobile,  # 手机号码
            # 'sign': '2683508eb4a77d5e34be219ba8f7fe90251e0346',
            'verifyCode': '451017'  # 验证码
        }

        response = requests.post('https://api.juzikong.com/mobi/u1/auth/mobileLogin',
                                 headers=headers, data=data, verify=False)


class GetJuzhi(object):
    '''
    获取句子类
    '''

    def __init__(self) -> None:
        '''
        初始化类,
        '''
        self.headers = {
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjI3NTU5MzYsInV1aWQiOiI4ZDNmYjEzYS0wM2FkLTQ0ODQtODhjMy1mZGVkZmRhNTRkNTUiLCJ1c2VybmFtZSI6IlppUGlSUlVBIiwibmJmIjoxNjI1NzIxMjgyLCJpYXQiOjE2MjU3MjEyODIsImV4cCI6MTY1NzI1NzI4MiwiaXNzIjoianV6aWtvbmctbWljcm8tc2VydmljZXMifQ.rr7_-g8ZfRKh7Ll53PbtIbycc1pbEHLsZKz_h8s5aIo',
            'User-Agent': 'axe/2.5.3 (build:2056;channel:huawei;Android6.0;EMUIEmotionUI_4.0.1)zh_CN',
            'n2c': 'axe',
            'n2v': '2.5.3',
            'n2p': 'android',
            'n2token': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjI3NTU5MzYsInV1aWQiOiI4ZDNmYjEzYS0wM2FkLTQ0ODQtODhjMy1mZGVkZmRhNTRkNTUiLCJ1c2VybmFtZSI6IlppUGlSUlVBIiwibmJmIjoxNjI1NzIxMjgyLCJpYXQiOjE2MjU3MjEyODIsImV4cCI6MTY1NzI1NzI4MiwiaXNzIjoianV6aWtvbmctbWljcm8tc2VydmljZXMifQ.rr7_-g8ZfRKh7Ll53PbtIbycc1pbEHLsZKz_h8s5aIo',
            'n2deviceId': '0866693028533631300003803900CN01',
            'n2uuid': '8d3fb13a-03ad-4484-88c3-fdedfda54d55',
            'n2brand': 'HUAWEI',
            'n2model': 'HUAWEI GRA-TL00',
            'n2os': 'Android6.0',
            'Host': 'api.juzikong.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
        }

    def get_meirishiju(self):
        '''
        获取首页推荐的每日十句
        '''
        url = "https://api.juzikong.com/mobi/home/posts/meirishiju"
        response = requests.get(url, headers=self.headers, verify=False)
        return response.json()

    def get_tuijian(self) -> dict:
        '''
        获取推荐的所有句子(未登录)
        '''
        url = "https://api.juzikong.com/mobi/m/topic2/recommendExplore"
        params = (
            ('start', '10'),
            ('limit', '9999999'),
            ('requestCount', '5'),
            ('timestamp', '%s' % (int(time.time()))),
            # ('sign', 'a6b3430dde6c6b252a08d7bc4950d904dcf43b5a'),
        )

        try:
            response = requests.get(url, headers=self.headers,
                                    params=params, verify=False)
            if str(response.json().get("success")) == "false" or None:
                print("推荐接口请求有误", response.json().get("message"))
                return None
                # with open("result1.json", "w", encoding="utf8") as j:
                #     j.write(str(response.text))
        except Exception as e:
            print("句子获取错误", e)
        else:
            return response.json()


if __name__ == "__main__":
    GetJuzhi().get_tuijian()
