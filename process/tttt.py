# -coding:UTF8-*-
import urllib2, urllib
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy

from operation.element import *
import os,time,unittest

ncols = 0
nrows = 0
# 读取Excel(需要安装xlrd)
fname = "I:\\fengzhuang\\process\\tte.xls"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
    sh = bk.sheet_by_name("Sheet1")
except:
    print "没有表名" % fname
# 获取行数
# global nrows
nrows = sh.nrows
# 获取列数
# global ncols
ncols = sh.ncols

def sac(j):
    print "nrows %d, ncols %d" % (nrows, ncols)
    row_list = []
    # 获取各行数据
    for i in range(j, ncols):
        row_data = sh.row_values(i)
        row_list.append(row_data)
    arr = row_list[0]
    global name
    global password
    arr1 = str(arr[1])                 # 转字符串
    name = arr1[:-2]
    arr2 = str(arr[2])                 # 转字符串
    password = arr2[:-2]
    print name,password                    # 用户名与密码（全局变量）


k = 0
el = Element()
class Case2(unittest.TestCase):
    u'''登录测试'''
    def login(self,Phone,Verification_code):
        el.sony()
        el.send_keys_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.EditText[1]',Phone)
        pd = el.Compare_the_text('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.EditText[1]',Verification_code)
        print u'输入手机号是否正确',pd
        el.send_keys_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.widget.EditText[1]',Verification_code)
        el.get_name(u'登录').click()  #点击登录按钮
        el.wait(5)
        Login_successful = el.To_compare(u'签到送3个积分') #判断是否登录成功
        return Login_successful



    # 循环+1
    @classmethod
    def setUp(self):
        global k
        sac(k)
        k += 1
        if k==3:
            k = 0



    def test01(self):
        u'''用户名为空，密码为空----登录失败'''
        el.get_name(u'选择小区').click()
        a = self.login(name,password)
        self.assertFalse(a, False)
        print '登录失败，手机号或验证码不正确。'

    def test02(self):
        u'''用户名为15100000000，密码为空----登录失败'''
        a = self.login(name, password)
        self.assertFalse(a, False)
        print '登录失败，手机号或验证码不正确。'


    def test03(self):
        u'''用户名为空，密码为1234----登录失败'''
        a = self.login(name, password)
        self.assertFalse(a, False)
        print '登录失败，手机号或验证码不正确。'


    def test04(self):
        u'''用户名为15100000000，密码为1234----登录成功'''
        a = self.login('15100000000', '1234')
        self.assertTrue(a, True)
        print '登录成功。'
        el.wait(5)
        el.get_name(u'我的').click()  # 点击我的
        el.get_xpath('//android.widget.RelativeLayout/android.widget.ImageView[2]').click()  # 设置
        el.get_name(u'退出此账号').click()  # 退出此账号
        el.get_name(u'确认').click()
        el.wait(5)
        a = el.To_compare(u'签到送3个积分')
        self.assertTrue(a, True)
        el.wait(5)




class Case1(unittest.TestCase):
    u'''预约流程'''
    def login(self,Phone,Verification_code,than):
        el.sony()
        el.send_keys_xpath(
            '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.EditText[1]',
            Phone)
        pd = el.Compare_the_text(
            '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.EditText[1]',
            Phone)
        print '输入手机号是否正确', pd
        el.send_keys_xpath(
            '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.widget.EditText[1]',
            Verification_code)
        el.get_name('登录').click()  # 点击登录按钮
        el.wait(5)
        Login_successful = el.To_compare(than)  # 判断是否登录成功
        print Login_successful
        self.assertTrue(Login_successful, True)
        el.wait(5)

    def xz(self):
        el.wait(5)
        el.appium()
        el.wait(5)
        el.get_name('搜素小区').click()  # 点击搜索
        # el.get_id('com.chengshe.huiaj:id/et_search_text').click() # 输入小区名称
        el.wait(5)
        # el.send_keys_id('com.chengshe.huiaj:id/et_search_text',u"星河世纪")
        el.get_name('选择小区').send_keys(u"星河世纪")
        el.wait(5)
        el.get_xpath('//android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').click()
        el.get_name('重新选择').click()
        el.get_xpath('//android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').click()
        el.get_name('确定').click()
        el.wait(5)
        a = el.To_compare('小区一元购会员名额已经抢光啦！')
        self.assertTrue(a, True)
        el.get_name('首页').click()


    # def tearDown(self):
    def tD(self):
        el.get_name(u'我的').click()  # 点击我的
        el.get_xpath('//android.widget.RelativeLayout/android.widget.ImageView[2]').click()  # 设置
        el.get_name(u'退出此账号').click()  # 退出此账号
        el.get_name(u'确认').click()
        el.wait(5)
        a = el.To_compare(u'选择小区')
        self.assertTrue(a, True)
        el.wait(5)


    def test01(self):
        u'''手机号：15770000046 验证码1234 --通过弹窗预约 --注册星河世纪小区'''
        el.get_name(u'选择小区').click()
        self.login('15760000046', '1234',u'请选择小区，享受汇爱家服务')
        el.get_name('去选择').click()           # 点击去选择
        self.xz()
        self.tD()


    def test02(self):
        u'''手机号：15770000043 验证码1234 --通过点击首页选择小区进行预约 --注册星河世纪小区'''
        el.get_name(u'选择小区').click()
        self.login('15760000043', '1234',u'请选择小区，享受汇爱家服务')
        el.get_name('取消').click() # 点击取消
        el.get_name('选择小区').click()  #
        self.xz()
        self.tD()


    def test03(self):
        u'''手机号：15770000044 验证码1234 --通过点击签到进行预约 --注册星河世纪小区'''
        el.get_name(u'选择小区').click()
        self.login('15770000044', '1234',u'请选择小区，享受汇爱家服务')
        el.get_name('取消').click()
        el.get_name('签到').click()    # 点击签到
        el.get_name('取消').click()    # 点击取消
        el.get_name('签到').click()    # 点击签到
        el.get_name('去选择').click()  # 点击去选择
        self.xz()
        self.tD()


    def test04(self):
        u'''手机号：15770000045 验证码1234 --通过爱家餐桌预约 --注册星河世纪小区'''
        el.get_name(u'选择小区').click()
        self.login('15770000045', '1234',u'请选择小区，享受汇爱家服务')
        el.get_name('取消').click()
        el.get_xpath('//android.widget.TabWidget/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()   #点击爱家餐桌
        el.get_xpath('//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[6]').click()  # 点击立即购买按钮
        el.get_name('去选择').click()        # 点击去选择
        self.xz()
        self.tD()