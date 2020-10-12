import json

import requests


login_url = "http://139.196.236.6:8080/user/login"

#账号密码登录
# login_form_Date = {"phoneNumber": "15038118649","passwd": "yuan1234"}
#
# passwd_r = requests.post(login_url,data=login_form_Date)
#
# print(passwd_r.status_code)
# print(passwd_r.text)
# m = passwd_r.json()
# print(m["data"]["userId"])

#验证码登录
login_form_Data = {"phoneNumber": "15038118649","vcode": "","message":"202010"}
code_r = requests.post(login_url,data=login_form_Data)
print(code_r.text)
cookies = {"ZHONGKEHUAIBEI":code_r.cookies["ZHONGKEHUAIBEI"]}

#获取个人订单
url = "http://139.196.236.6:8080/payOrder/selectAllByMine"
r = requests.get(url,cookies=cookies)
print(r.text)