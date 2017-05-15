#!/usr/bin/python
# -*- coding: UTF-8 -*-
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import datetime
import time
import os


def mk():
    # sender = '18216060753@139.com'       # 发件人1804882096@qq.com
    sender = 'leiyong711@aliyun.com'
    receivers = '1804882096@qq.com'    # 接收邮件，可设置为你的QQ邮箱或者其他邮箱leiyong711@163.com
    my_pass = 'leiyong711'  # 授权码'ibiaowujreplcbhf'

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("Last_indulge", 'utf-8')  # 发件人名字Last indulge
    message['To'] = Header(receivers, 'utf-8')  # 收件人名字
    subject = '测试报告'  # 邮件主题
    message['Subject'] = Header(subject, 'utf-8')
    # 邮件正文内容
    Time = str(datetime.datetime.now())[:-7]
    timestr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
    directory1 = '..\\The_report\\' + timestr[:10] + '\\' + timestr[11:] + '\\log\\'
    directory = os.listdir(directory1)
    for i in range(len(directory)):
        if str(directory[i]).find(".xls") != -1:
            The_attachment = directory[i]
    nei = '以下是%s分执行后的测试版报告，该附件包含：' \
          '\n• 测试信息汇总：%s' \
          '\n• 用例执行结果：Case_report.html' \
          '\n• 错误日志：Equipment_information.txt' \
          '\n• 测试错误截图：psb.png' %(Time,The_attachment)
    message.attach(MIMEText(nei, 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 测试汇总 文件
    att1 = MIMEText(open(directory1 + The_attachment, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename=' + The_attachment     # 附件别名
    message.attach(att1)

    # 构造附件2，传送当前目录下的 runoob.txt 文件
    The_attachment2 = 'Case_report.html'
    timestr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
    att2 = MIMEText(open( '..\\The_report\\' + timestr[:10] + '\\' + timestr[11:] + '\\Case_report\\'+The_attachment2, 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename='+The_attachment2
    message.attach(att2)

    # 构造附件3，传送当前目录下的 runoob.txt 文件
    The_attachment3='Equipment_information.txt'
    timestr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
    att3 = MIMEText(open('..\\The_report\\' + timestr[:10] + '\\' + timestr[11:] + '\\log\\'+The_attachment3, 'rb').read(), 'base64', 'utf-8')
    att3["Content-Type"] = 'application/octet-stream'
    att3["Content-Disposition"] = 'attachment; filename='+The_attachment3
    message.attach(att3)

    try:
        server = smtplib.SMTP("smtp.aliyun.com", 25)  # 发件人邮箱中的'SMTP'服务器，端口是25
        server.login(sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender, [receivers, ], message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        # 关闭连接
        server.quit()
        print "邮件发送成功"

    except smtplib.SMTPException:
        print "无法发送邮件"
