# -*- coding:utf-8 -*-
from folder_Path import *
import time
import os
import re
import xlwt
import datetime

start = 0

class test_Time:
    def start(self,name):
        global start
        start = name
        print '计时开始时间：%s' % start


def Load_test_configuration():
    '''写入excel表格'''
    ks = datetime.datetime.now()
    Program_location = 'F:\\haj.apk'

    class pptp:

        # 获取手机信息
        def Phone_Information(self):

            # 手机信息正则限制
            def modified(name):
                try:
                    reu = list(os.popen(name).readlines())
                    return re.findall('.*', reu[0])[0]  # ([^\s\\\]+)
                except:
                    return 'Get error'
            brand = modified('adb shell getprop ro.product.brand')                       # 读取手机品牌
            phone_models = modified('adb shell getprop ro.semc.product.name')            # 读取设备型号
            deviceVersion = modified('adb shell getprop ro.build.version.release')       # 读取设备系统版本号
            readDeviceId = list(os.popen('adb devices').readlines())                     # 读取设备 id
            devices = str(readDeviceId[1])[:-8]                                          # 正则表达式匹配出 id 信息
            # devices = re.findall(r'^\w*\b', readDeviceId[1])[0]                         # 正则表达式匹配出 id 信息

            return brand,phone_models,deviceVersion,devices      # 返回品牌、型号、系统版本、设备id

        # 得到运行内存
        def get_men_total(self,devices):
            cmd = "adb -s "+devices+ " shell cat /proc/meminfo"
            get_cmd = os.popen(cmd).readlines()
            men_total = 0
            men_total_str = "MemTotal"
            for line in get_cmd:
                if line.find(men_total_str) >= 0:
                    men_total = line[len(men_total_str) +1:].replace("kB", "").strip()
                    break
            ram = int(men_total) / 1024
            return str(ram) + "MB"

        # 得到CPU核心数
        def get_cpu_kel(self,devices):
            cmd = "adb -s " +devices +" shell cat /proc/cpuinfo"
            get_cmd = os.popen(cmd).readlines()
            find_str = "processor"
            int_cpu = 0
            for line in get_cmd:
                if line.find(find_str) >= 0:
                    int_cpu += 1
            return str(int_cpu) + "核"

        # 得到手机分辨率
        def get_app_pix(self,devices):
            try:
                result = os.popen("adb -s " + devices+ " shell wm size", "r")
                return result.readline().split("Physical size:")[1]
            except:
                return 'Get error'

        # 常用的性能监控
        def top_cpu(devices, pkg_name):
            cmd = "adb -s " + devices + " shell dumpsys cpuinfo | grep -w " + pkg_name + ":"
            get_cmd = os.popen(cmd).readlines()
            for info in get_cmd:
                return float(info.split()[2].split("%")[0])

        # 得到men的使用情况
        def get_men(devices, pkg_name):
            cmd = "adb -s " + devices + " shell  dumpsys  meminfo %s" % (pkg_name)
            total = "TOTAL"
            get_cmd = os.popen(cmd).readlines()
            for info in get_cmd:
                info_sp = info.strip().split()
                for item in range(len(info_sp)):
                    if info_sp[item] == total:
                        return int(info_sp[item + 1])
            return 0

        # 电量信息
        def Battery_capacity(self):
            get_cmd = os.popen("adb shell dumpsys battery").readlines()
            for i in range(0, len(get_cmd)):
                a = str(get_cmd[i])
                b = 'level'
                p = a.find(b)
                try:
                    if p != -1:
                        s = get_cmd[i].split('level')
                        Battery = "".join(s).strip('\n').strip("'").strip('  : ')
                        return int(Battery)
                except:
                    return '获取电量失败'

    # 查询app信息
    def ApkInfo(address, search):
        aapt = list(
            os.popen('I:\\android-sdk-windows\\build-tools\\18.1.0\\aapt dump badging ' + address).readlines())
        for i in range(0, len(aapt)):           # 遍历列表
            a = str(aapt[i])                    # 列表转字符串
            sStr2 = search                      # 要查询的字符串
            p = a.find(sStr2)                   # 判断字符串是否存在，不存在赋值-1
            if p != -1:
                result = aapt[i].split(search)[1:]           # 获取查询参数在列表中的索引截取参数值
                if search == 'launchable-activity: name=':   # 判断是否查询包名
                    result = result[0].split("label=")[:1]   # 如果是查询启动类就截取“label”前的值
                if search == 'package: name=':               # 判断是否查询包名
                    result = result[0].split("versionCode=")[:1]            # 如果是查询包名就截取“versionCode=”前的值
                App_Information = "".join(result).strip('\n').strip("'")    # 去掉字符串中的换行与'号
                return App_Information.strip().lstrip().rstrip("'")         # 去空格及特殊符号并返回查询结果

    global application_Name
    global application_Version
    global appPackage
    global appActivity
    application_Name = ApkInfo(Program_location, 'application-label:')  # 获取应用名
    application_Version = ApkInfo(Program_location, 'versionName=')           # 获取应用版本信息
    appPackage = ApkInfo(Program_location, 'package: name=')                  # 获取应用包名
    appActivity = ApkInfo(Program_location, 'launchable-activity: name=')     # 获取启动类

    global FileSize
    size = os.path.getsize(Program_location)               # 获取应用程序大小
    FileSize = round(size / 1024 / 1024.0, 2)           # 转大小单位
    FileSize = str(FileSize) + 'MB'

    # 应用名、应用版本、应用大小、应用包名、启动类、
    application = [application_Name,application_Version,FileSize,appPackage,appActivity]
    global tt
    tt = pptp()
    global arr
    global arr2
    global arr3

    global StartBc
    StartBc = tt.Battery_capacity()
    # 品牌、型号、系统版本、设备id
    arr3 = tt.Phone_Information()

    arr = ["手机品牌","手机型号","系统版本","CPU核心数","运行内存大小","手机分辨率","测试期间耗电"]

    # 品牌、型号、系统版本、CPU核心数、运行内存、手机分辨率
    arr2 = [arr3[0],arr3[1],arr3[2],tt.get_cpu_kel(arr3[3]),tt.get_men_total(arr3[3]),tt.get_app_pix(arr3[3])]


    # 返回品牌、型号、系统版本、设备id、应用名、应用版本信息、应用包名、启动类
    return arr3[0], arr3[1], arr3[2], arr3[3], application_Name, application_Version, appPackage, appActivity

def Excel(case_Result):
    # excel样式
    def set_style(name, height, bold):
        u'字体，高度，背景色，加粗，字体色'
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = name  # 'Times New Roman'
        font.bold = bold
        font.color_index = 4
        font.height = height
        style.font = font

        alignment = xlwt.Alignment()  # Create Alignment
        alignment.horz = xlwt.Alignment.HORZ_CENTER  # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
        alignment.vert = xlwt.Alignment.VERT_CENTER
        style.alignment = alignment
        return style

    def s_style(name, height,lei,bold,s):
        u'字体，高度，背景色'
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = name  # 'Times New Roman'
        font.colour_index = s  # 设置其字体颜色
        font.bold = bold
        font.color_index = 4
        font.height = height
        style.font = font
        alignment = xlwt.Alignment()  # Create Alignment
        alignment.horz = xlwt.Alignment.HORZ_CENTER  # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
        alignment.vert = xlwt.Alignment.VERT_CENTER
        style.alignment = alignment
        pattern = xlwt.Pattern()  # Create the Pattern
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
        pattern.pattern_fore_colour = lei
        style.pattern = pattern  # Add Pattern to Style创建模式
        return style

    w = xlwt.Workbook()             # 创建一个工作簿
    ws = w.add_sheet('Hey, Hades')  # 创建一个工作表

    # 合并单元格
    ws.write_merge(0,0,0,4,u'测试报告总概况',set_style(u'宋体',360,True))         # 合并行单元格
    ws.write_merge(1,1,0,4,u'测试概况',s_style(u'宋体',270,4,False,0x01))         # 合并行单元格
    ws.write_merge(8,8,0,6,u'测试手机详情',s_style(u'宋体',270,4,False,0x01))     # 合并行单元格

    alignment = xlwt.Alignment() # Create Alignment
    alignment.horz = xlwt.Alignment.HORZ_CENTER # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
    alignment.vert = xlwt.Alignment.VERT_CENTER # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
    style = xlwt.XFStyle() # Create Style
    style.alignment = alignment # Add Alignment to Style

    end = datetime.datetime.now()
    print '计时结束时间：%s' % end
    Time_consuming = str(end - start)[:-7]  # 用测试结束时间-开始时间得到测试耗时，再把时间转成字符串并去掉小数部分
    print '测试耗时：%s' % Time_consuming

    End_BC = tt.Battery_capacity()
    BC = str(StartBc - End_BC)+'%'
    arr2.append(BC)
    app1 = ["APP名称",application_Name,"用例总数",case_Result[0],"脚本语言"]
    app2 = ["APP大小",FileSize,"通过总数",case_Result[1]]
    app3 = ["APP版本",application_Version,"失败总数",str(int(case_Result[2]) + int(case_Result[3]))]
    app4 = ["测试日期",time.strftime( '%Y-%m-%d %H:%M:%S', time.localtime(time.time())),"测试耗时",Time_consuming + "秒"]

    ws.write_merge(3,5,4,4,'appium+python',set_style(u'宋体',270,False)) #合并行单元格

    for i in range(0,len(app1)):
        ws.write(2, i, app1[i].decode('utf-8'),set_style(u'宋体',270,False))
    for i in range(0,len(app2)):
        ws.write(3, i, app2[i].decode('utf-8'),set_style(u'宋体',270,False))
    for i in range(0,len(app3)):
        ws.write(4, i, app3[i].decode('utf-8'),set_style(u'宋体',270,False))
    for i in range(0,len(app4)):
        ws.write(5, i, app4[i].decode('utf-8'),set_style(u'宋体',270,False))

    for i in range(0,len(arr)):     # 写入第一行arr的内容
        ws.write(9, i, arr[i].decode('utf-8'),set_style(u'宋体',270,False))
    for i in range(0,len(arr2)):    # 写入第二行arr2的内容
        ws.write(10, i, arr2[i].decode('utf-8'),set_style(u'宋体',270,False))

    Create_folder('..\\The_report\\', '\\log')     # 判断文件夹是否存在，不存在则创建
    timestr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
    b = '..\\The_report\\' + timestr[:10] + '\\' + timestr[11:] + '\\log\\'+ arr3[0].strip("\r") +'_'+ arr3[1].strip("\r").replace(' ','_') + ".xls"  #  '_' +application_Name + _测试报告总概况  " ..\\The_report\\log\\" + arr3[0].strip("\r") +'_'+ arr3[1].strip("\r") + '_' +application_Name +"_测试报告总概况.xls"
    w.save(b.decode('utf-8')) # 以“品牌_机型”命名保存

    print '导出结束'











