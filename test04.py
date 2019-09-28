#coding=utf-8

import sys
temp = sys.stdout

#这里的sys.stdout也就是我们python中标准输出流，这个标准输出流默认是映射到打开脚本的窗口的，所以，我们的print操作会把字符打印到屏幕上。
#我们通过修改这种映射关系,把我们的打印操作重定向到其它地方，例如特定的文件。方法就是给sys.stdout赋值，修改它的指向。
sys.stdout = open('test.txt','w')
print 'hello world'

#恢复默认映射关系
sys.stdout = temp 
print 'nice'