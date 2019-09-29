#coding=utf-8

# w新建只写，w+新建读写，二者都会将文件内容清零
fd = open("test00_read_write.txt",'w+')
fd.write('123')

# r+：可读可写，若文件不存在，报错；
fd = open("test00_read_write.txt",'r+')
fd.write('456')

# a+: 追加内容
fd = open("test00_read_write.txt",'a+')
fd.write('789')

# test00_read_write.txt 文件的最终内容应该是 456789
