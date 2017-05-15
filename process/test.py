# -*- coding:utf-8 -*-
import time
from operation.element import Element
import unittest #想使用unittest框架，首先要引入unittest 包，这个不多解释。
import os

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(file), p))


el = Element()
Phone = '151 0000 00000000000000000'
Verification_code = '2000'
index = 1
class Dttest(unittest.TestCase):

    png_file = '..\\The_report\\er_img\\'

    # def setUp(self):
    #     el.Error_screenshot()
    #     print '截图'
    #     self.verificationErrors = []
    #     self.accept_next_alert = True

    def tearDown(self):
        el.Error_screenshot()
        print '截图'

    #     self.assertEqual([], self.verificationErrors)


    @classmethod
    def login(self):
        u'''测试登录'''
        # try:
        el.get_name(u'选择小区').click()
        # self.tearDown()
        el.send_keys_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.EditText[1]',Phone)
        pd = el.Compare_the_text('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.EditText[1]','151 0000 0000')
        print '输入手机号是否正确',pd
        el.send_keys_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.widget.EditText[1]',Verification_code)
        el.get_name('登录').click()  #点击登录按钮
        time.sleep(2)
        Login_successful = el.To_compare(u'签到送3个积分') #判断是否登录成功
        print Login_successful
        # print 'logingeshi=', type(Login_successful)
        # time.sleep(3)


        # if Login_successful == True: #如果相等则登录成功
        #     print '登录成功'
        # self.assertEqual(True,True)#如果相等则登录成功
        # self.assertTrue(Login_successful)
        print '登录成功'
        # except:
        #     print '登录失败'
        #     el.Error_screenshot("登录测试用例")            #调用截图方法

    @classmethod
    def hd(self):
        u'''滑动'''
        time.sleep(4)
        el.get_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.TabHost[1]/android.widget.LinearLayout[1]/android.widget.TabWidget[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
        timestr = time.strftime('%H%M', time.localtime(time.time()))
        a = int(timestr)
        c = a < 1830
        d = a > 0
        if c & d == False:
            print '时间外%s' % a
            el.get_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.TextView[1]').click()
        else:
            print '时间内%s' % a
        time.sleep(2)
        el.swipeLeft(1000)
        time.sleep(1)
        el.swipeLeft(1000)
        time.sleep(1)
        el.swipeLeft(1000)
        time.sleep(1)
        el.swipeLeft(1000)
        time.sleep(1)
        el.swipeRight(1000)
        time.sleep(1)
        el.swipeRight(1000)

    @classmethod
    def tuichu(self):
        u'''退出登录'''
        time.sleep(5)
        el.get_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.TabHost[1]/android.widget.LinearLayout[1]/android.widget.TabWidget[1]/android.widget.RelativeLayout[4]').click()
        el.get_id('com.chengshe.huiaj:id/userf_setting').click()
        el.get_id('com.chengshe.huiaj:id/user_exit_layout').click()
        el.get_id('com.chengshe.huiaj:id/tv_simple_dialog_left').click()
        time.sleep(2)
        el.To_compare(u'签到送3个积分')  # 判断是否登录成功
        # Login_successful = el.To_compare(u'签到送3个积分')  # 判断是否登录成功
        # print 'logingeshi=',type(Login_successful)
        # time.sleep(3)
        # self.assertTrue(Login_successful)
        # self.assertEqual('a', 'a')  # 如果相等则登录成功
        print '退出成功'
        el.quit()
