# -coding:UTF8-*-
import urllib2, urllib
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy

ncols = 0
nrows = 0
# 读取Excel(需要安装xlrd)
fname = "tte.xls"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
    sh = bk.sheet_by_name("Sheet1")
except:
    print "没有表名" % fname
def a(j):
    # 获取行数
    global nrows
    nrows = sh.nrows
    # 获取列数
    global ncols
    ncols = sh.ncols
    print "nrows %d, ncols %d" % (nrows, ncols)
    row_list = []
    # 获取各行数据
    for i in range(j, ncols):
        row_data = sh.row_values(i)
        row_list.append(row_data)
    arr = row_list[0]
    name = arr[1]
    password = arr[2]
    print name,password                    # 用户名与密码（全局变量）

k = 0
global k

for i in range(nrows):              # 循环执行用例login  直到该用例的数据全部执行完毕跳到下一条用例
    a(1)                            # 调用第一行的所有数据（K为当前读取的行数）
    k += 1
