#coding=utf-8

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

log = open('log.txt','a')
print >> log,'hello world' #重定向到文件log.txt中
print 'hello world' #输出到默认位置
