# -*- coding:utf-8 -*-

import sys

import logging
import HTMLTestRunner
from The_benchmark.Test_summary import *
from The_benchmark.kdks import *
from process.tttt import *
# from process.hd import *
reload(sys)
sys.setdefaultencoding('utf8')
# from process.test import *

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(file), p))

Create_folder('..\\The_report\\', '\\log')
timestr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
b = '..\\The_report\\' + timestr[:10] + '\\' + timestr[11:] + '\\log\\'
logpath=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"log")
logging.basicConfig(
                    level=logging.DEBUG,
                    # level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%y-%m-%d %H:%M',
                    filename=os.path.join(logpath, b+'log.txt'),
                    filemode='a')

# sys.stderr = open('..\\The_report\\log\\python.txt', 'w')
# print >>sys.stderr, 'hello exception'
#
# tesst()
# end = time.clock()
# print('运行耗时: %s S'%(end-start))
# te = tesst()
# te.login()
# end = time.clock()
# print ('运行耗时：%s S'%(end-start))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(Dttest('login'))
    # suite.addTest(Dttest('hd'))
    # suite.addTest(Dttest('tuichu'))
    logging.error("出错啦")
    suite.addTest(Case2('test01'))
    logging.warning("警告")
    logging.info("运行")
    logging.debug("调试")
    suite.addTest(Case2('test02'))
    suite.addTest(Case2('test03'))
    suite.addTest(Case2('test04'))
    suite.addTest(Case1('test01'))
    suite.addTest(Case1('test02'))
    suite.addTest(Case1('test03'))
    suite.addTest(Case1('test04'))
    timestr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
    Create_folder('..\\The_report\\', '\\Case_report')  # 判断文件夹是否存在，不存在则创建
    filename = '..\\The_report\\'+ timestr[:10]+ '\\' + timestr[11:] + '\\Case_report\\' + 'Case_report.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='Appium自动化测试结果',
    description='测试报告'
    )
    runner.run(suite)
    ass = HTMLTestRunner.leiyong123  # 获取HTMLTestRunner.leiyong123返回的用例执行数量与结果
    fp.close()                       # 测试报告关闭
    print ass
    Excel(ass)                       # 调用生成测试信息Excel
    time.sleep(5)                    # 延时5秒
    mk()                             # 调用发送邮件


# adb shell settings put secure default_input_method com.baidu.input/.ImeService
# adb shell settings put secure default_input_method io.appium.android.ime/.UnicodeIME











