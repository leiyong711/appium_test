# -*- coding:utf-8 -*-

from The_benchmark.folder_Path import *

import time
import sys
import os

reload(sys)

co = 1
sys.setdefaultencoding('utf8')

from The_benchmark.driver import AppiumTest

#元素封装
class Element:

    def __init__(self):
        at = AppiumTest()
        self.driver = at.get_driver()

    #id定位元素
    def get_id(self,id):
        element = self.driver.find_element_by_id(id)
        # print (id + '操作成功')
        return element

    # name定位元素
    def get_name(self,name):
        element = self.driver.find_element_by_name(name)
        # print (name + '操作成功')
        return element

    # xpath定位元素
    def get_xpath(self,xpath):
        element = self.driver.find_element_by_xpath(xpath)
        # print ('xpath操作成功')
        return element

    #获取元素的文本值
    def get_text(self,text):
        element = self.driver.find_element_by_id(text).text
        print ( '获取文本成功，内容：' + element)
        return element

    #元素赋值
    def send_keys_id(self,id,key):
        element = self.driver.find_element_by_id(id).send_keys(key)
        print ('输入内容成功，内容：' + key)
        return element

    def send_keys_xpath(self,xpath,key):
        element = self.driver.find_element_by_xpath(xpath).send_keys(key)
        print ('输入内容成功，内容：' + key)
        return element

    # 获取屏幕宽和高
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        print x,y
        return (x, y)

    # 从右向左滑动
    def swipeLeft(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.25)
        self.driver.swipe(x1, y1, x2, y1,t)

    # 从左向右滑动
    def swipeRight(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.25)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1,t)

    # 从下向上滑动
    def swipeUp(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.75)
        y2 = int(l[1] * 0.25)
        self.driver.swipe(x1, y1, x1, y2, t)

    # 从上向下滑动
    def swipeDown(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2, t)

    # 查找元素，没找到就滑动
    def findLocal(self,name):
        x = 1
        while x == 1:
            if self.fact(name) ==1:
                self.swipeUp(10)
                time.sleep(2)
                self.fact(name)
            else:
                print '找到了'
                x = 2

    # 递归查找
    def fact(self,name):
        n = 1
        try:
            self.driver.find_element_by_name().click()
        except:
            return n

    #退出app
    def over(self):
        element = self.driver.quit()
        return element


    #判断输入结果与实际结果
    def Compare_the_text(self,id,expected):
        The_actual = self.driver.find_element_by_xpath(id).text  # "获取实际输入验证码"
        if expected == The_actual:
            return True
        else:
            return False

    #比较元素
    def To_compare(self,name):
        try:
            element = self.driver.find_element_by_name(name)
            t = element.is_enabled()
            print '元素比对t结果%s'% t
            return t
        except:
            return False

    #报错并截图
    # def Error_screenshot(self,name):
    #     print '-----------------'
    #     ti = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    #     self.driver.get_screenshot_as_file('E:\\Testreport\\png\\' + name.decode('utf-8') + ti + '.jpg')
    #     print (name + '失败请到D盘tupian目录下查看"'+ name.decode('utf-8') + ti +'"错误截图')

    def Error_screenshot(self):
        print '-----------------'
        global co
        cou = str(co)
        ti = time.strftime('%Y%m%d', time.localtime(time.time()))
        timestr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
        Create_folder('..\\The_report\\', '\\er_img')   # 判断文件夹是否存在，不存在则创建
        self.driver.get_screenshot_as_file('..\\The_report\\' + timestr[:10] + '\\' + timestr[11:] + '\\er_img\\'+ ti +'_'+ cou +'.png') # '..\\The_report\\er_img\\'+ ti +'_'+ cou +'.png'
        co +=1
        print ('失败请到..\\The_report\\' + timestr[:10] + '\\' + timestr[11:] + '\\er_img\\目录下查看"'+ ti +'"错误截图')

    #关闭程序
    def quit(self):
        self.driver.quit()
        print ('关闭app')


    # 方法运行时间
    def time_me(fn):
        def _wrapper(*args, **kwargs):
            start = time.clock()
            fn(*args, **kwargs)
            print "%s cost %s second" % (fn.__name__, time.clock() - start)

        return _wrapper

    # 隐示等待
    def stime(self,ti):
        self.driver.implicitly_wait(ti)

    # 切换appium输入法      查询输入法（ime list -s）
    def appium(self):
        os.popen('adb shell "ime set io.appium.android.ime/.UnicodeIME"')

    # 切换Xperia国际输入法
    def sony(self):
        # 索尼国际输入法
        # os.popen('adb shell "ime set com.sonyericsson.textinput.uxp/.glue.InputMethodServiceGlue"')
        # 夜神模拟器
        # os.popen('adb shell "ime set com.example.android.softkeyboard/.SoftKeyboard"')
        # 逍遥模拟器
        os.popen('adb shell "ime set com.microvirt.memuime /.MemuIME"')

    # 隐示等待
    def wait(self,t):
        self.driver.implicitly_wait(t)

