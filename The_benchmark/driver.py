# -*- coding:utf-8 -*-
from appium import webdriver
from Test_summary import *
from folder_Path import *
import time
import os
import re
import sys
import datetime


reload(sys)
sys.setdefaultencoding('utf8')
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(file), p))


startTime = datetime.datetime.now()
bb = test_Time()
bb.start(startTime)

class AppiumTest:
    def __init__(self):
        def modified(name):
            reu = list(os.popen(name).readlines())
            return re.findall('.*', reu[0])[0]  # ([^\s\\\]+)

        # 返回品牌、型号、系统版本、设备id、应用名、应用版本信息、应用包名、启动类
        caps = Load_test_configuration()
        brand = caps[0]  # 品牌
        phone_models = caps[1]  # 型号
        deviceVersion = caps[2]  # 系统版本
        deviceId = caps[3]  # 设备id
        application_Name = caps[4]  # 应用名
        application_Version = caps[5]  # 应用版本信息
        appPackage = caps[6]  # 应用包名
        appActivity = caps[7]  # 启动类
        print '正在加载配置服务',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        desired_caps = {'platformName': 'Android',  # 手机平台
                        'platformVersion': deviceVersion,  # Android版本
                        'deviceName': deviceId,  # 设备ID   127.0.0.1:21503  CB5A2BJGAP
                        # 'app': 'F:\\haj.apk',
                        'appPackage': appPackage,  # 包名
                        'appActivity': appActivity,  # 类名
                        'unicodeKeyboard': True,   # 使用unicodeKeyboard的编码方式来发送字符串
                        'resetKeyboard': True  # 将键盘给隐藏起来
                        }
        timestr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
        Create_folder('..\\The_report\\', '\\log')  # 判断文件夹是否存在，不存在则创建
        title = '..\\The_report\\' + timestr[:10] + '\\' + timestr[11:] + '\\log\\' + 'Equipment_information'

        x = ["手机平台：Android \n手机品牌：%s \n手机型号：%s \n系统版本号：%s \n设备id：%s \n应用名：%s \n应用版本信息包：%s"
             " \n包名：%s \n类名：%s\n"
             % (brand,phone_models,deviceVersion,deviceId,application_Name,application_Version,appPackage,appActivity)]

        with open("%s.txt" % title, "a") as f:  # 格式化字符串还能这么用！
            f.write(
                "\n------------------------------------- %s -----------------------------------------\n"
                % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            for i in x:
                f.write(i)

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        print '正在启动程序',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        self.driver.implicitly_wait(8)

    def get_driver(self):
        return self.driver
