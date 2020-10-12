import unittest
import requests
import HTMLTestRunner

class LoginUnittest(unittest.TestCase):

    #前置
    def setUp(self):
        #获取session对象
        self.session = requests.session()
        self.login_url = "http://139.196.236.6:8080/user/login"

    #释放
    def tearDown(self):
        self.session.close()

    #登录成功
    def test_login_success(self):
        data = {"phoneNumber": "15038118649", "passwd": "yuan1234"}
        r = self.session.post(self.login_url,data=data)
        #断言
        try:
            self.assertEqual(None,r.json()["errmsg"])
            self.assertEqual(0,r.json()["errcode"])
        except AssertionError as e:
            print(e)

    #用户不存在啊
    def test_login_nouser(self):
        data = {"phoneNumber": "15038118648", "passwd": "yuan1234"}
        r = self.session.post(self.login_url,data=data)
        #断言
        try:
            self.assertEqual("用户不存在",r.json()["errmsg"])
        except AssertionError as e:
            print(e)

    #密码错误
    def test_login_errpasswd(self):
        data = {"phoneNumber": "15038118649", "passwd": "yuan1235"}
        r = self.session.post(self.login_url, data=data)
        # 断言
        try:
            self.assertEqual("密码错误", r.json()["errmsg"])
        except AssertionError as e:
            print(e)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(LoginUnittest("test_login_success"))
    suite.addTest(LoginUnittest("test_login_nouser"))
    suite.addTest(LoginUnittest("test_login_errpasswd"))
    filepath = "C:\\Users\\y\\Desktop\\测试报告.html"
    fp = open(filepath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"科创汇登录测试报告标题", description=u"2B项目")
    runner.run(suite)
    fp.close()