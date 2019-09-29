#coding=utf-8

# 测试：屏幕输出重定向到文件输出。

import sys

'''
class Test:
    def write(self,string):
        #do something you wanna do

t1 = Test()
temp = sys.stdout
sys.stdout = t1
print 'hello world'
'''

log = open('test05_log.txt','a')

#重定向到文件log.txt中
print >> log,'Hello world, the test for redirect to test05_log.txt'
print 'Hello world, the print output back to screen.' #输出到默认位置
