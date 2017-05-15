# -*- coding:utf-8 -*-
import os
import time
def Create_folder(folder_Path0,folder_Path1):
    timestr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
    # a = os.path.exists('..\\The_report\\' + timestr[:10] + '\\' + timestr[11:] + '\\Case_report')
    a = os.path.exists(folder_Path0 + timestr[:10] + '\\' + timestr[11:] + folder_Path1)
    if a == False:
        os.makedirs(folder_Path0 + timestr[:10] + '\\' + timestr[11:] + folder_Path1)
