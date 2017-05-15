# ecoding=utf-8
from operation.element import *
import os,time,unittest

el = Element()
class Case(unittest.TestCase):
    u'''登录测试'''
    def login(self,Phone,Verification_code):

        el.send_keys_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.EditText[1]',Phone)
        pd = el.Compare_the_text('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.EditText[1]',Verification_code)
        print '输入手机号是否正确',pd
        el.send_keys_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.widget.EditText[1]',Verification_code)
        el.get_name('登录').click()  #点击登录按钮
        time.sleep(2)
        Login_successful = el.To_compare(u'签到送3个积分') #判断是否登录成功
        return Login_successful
        # print 'logingeshi=', type(Login_successful)
        # time.sleep(3)
        # if Login_successful == True: #如果相等则登录成功
        #     print '登录成功'
        # self.assertEqual(True,True)#如果相等则登录成功




    def test01(self):
        u'''用户名为空，密码为空----登录失败'''
        el.get_name(u'选择小区').click()
        a = self.login('','')
        self.assertFalse(a, False)

    def test02(self):
        u'''用户名为15100000000，密码为空----登录失败'''
        a = self.login('15100000000', '')
        self.assertFalse(a, False)

    def test03(self):
        u'''用户名为空，密码为1234----登录失败'''
        a = self.login('', '1234')
        self.assertFalse(a, False)

    def test04(self):
        u'''用户名为15100000000，密码为1234----登录成功'''
        a = self.login('15100000000', '1234')
        self.assertTrue(a, True)
        time.sleep(3)
        el.get_name('我的')  # 点击我的
        el.get_id('com.chengshe.huiaj:id/userf_setting')  # 设置
        el.get_name('退出此账号')  # 退出此账号
        el.get_name('确认')
        time.sleep(2)
        a = el.To_compare('签到送3个积分')
        self.assertTrue(a, True)
        time.sleep(3)

class Case1(unittest.TestCase):
    u'''预约流程'''
    def login(self,Phone,Verification_code):
        el.send_keys_xpath(
            '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.EditText[1]',
            Phone)
        pd = el.Compare_the_text(
            '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.EditText[1]',
            Verification_code)
        print '输入手机号是否正确', pd
        el.send_keys_xpath(
            '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.widget.EditText[1]',
            Verification_code)
        el.get_name('登录').click()  # 点击登录按钮
        time.sleep(2)
        Login_successful = el.To_compare(u'签到送3个积分')  # 判断是否登录成功
        self.assertFalse(Login_successful, False)
        time.sleep(1)

    def xz(self):
        el.get_id('com.chengshe.huiaj:id/community_item_layout')  # 点击搜索
        el.get_id('com.chengshe.huiaj:id/et_search_text').click() # 输入小区名称
        el.send_keys_id('com.chengshe.huiaj:id/et_search_text',u'星河世纪')
        time.sleep(2)
        el.get_xpath('//android.widget.ListView[@resource-id=\"com.chengshe.huiaj:id/location_community_list\"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')
        el.get_name('重新选择')
        el.get_xpath('//android.widget.ListView[@resource-id=\"com.chengshe.huiaj:id/location_community_list\"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')
        el.get_name('确定')
        time.sleep(2)
        a = el.To_compare('小区一元购会员名额已经抢光啦！')
        self.assertTrue(a, True)
        el.get_name('首页')

    def td(self):
        time.sleep(3)
        el.get_name('我的')  # 点击我的
        el.get_id('com.chengshe.huiaj:id/userf_setting')  # 设置
        el.get_name('退出此账号')  # 退出此账号
        el.get_name('确认')
        time.sleep(2)
        a = el.To_compare('签到送3个积分')
        self.assertTrue(a, True)
        time.sleep(3)


    def test01(self):
        u'''登录后通过弹出预约小区--手机号：15710000002 验证码1234注册星河世纪小区'''
        self.login('15710000002', '1234')
        el.get_name('去选择') # 点击去选择
        el.get_id('com.chengshe.huiaj:id/community_item_layout') # 搜索
        self.xz()
        self.td()


    def test02(self):
        u'''登陆后通过点击首页选择小区进行预约--手机号：15710000003 验证码1234注册星河世纪小区'''
        self.login('15710000003', '1234')
        el.get_name('取消') # 点击取消
        el.get_name('选择小区')  #
        self.xz()
        self.td()


    def test03(self):
        u'''通过点击签到进行预约小区--手机号：15710000004 验证码1234注册星河世纪小区'''
        self.login('15710000004', '1234')
        el.get_id('com.chengshe.huiaj:id/iv_sign_layout') # 点击签到
        el.get_name('取消')  # 点击取消
        el.get_id('com.chengshe.huiaj:id/iv_sign_layout')  # 点击签到
        el.get_name('去选择')  # 点击去选择
        self.xz()
        self.td()


    def test04(self):
        u'''通过爱家餐桌预约小区--手机号：15710000005 验证码1234注册星河世纪小区'''
        self.login('15710000005', '1234')
        el.get_xpath('//android.widget.TabWidget[@resource-id=\"android:id/tabs\"]/android.widget.RelativeLayout[2]')#点击爱家餐桌
        el.get_xpath('//android.support.v7.widget.RecyclerView[@resource-id=\"android:id/list\"]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[6]')# 点击立即购买按钮
        el.get_name('去选择')  # 点击去选择
        self.xz()
        self.td()