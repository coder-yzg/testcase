import requests

login_url = "http://139.196.236.6:8080/user/login"
login_form_Date = {"phoneNumber": "15038118649","passwd": "yuan1234"}

#获取session对象
session = requests.session()

#账号密码登录
r = session.post(login_url,data=login_form_Date)
print(r.text)

#获取个人订单
order_url = "http://139.196.236.6:8080/payOrder/selectAllByMine"
r1 = session.get(order_url)
print(r1.text)