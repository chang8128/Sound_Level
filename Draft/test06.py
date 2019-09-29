#coding=utf-8

# 测试：记录程序过程到文本文件。

import sys 

class Logger(object):   
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN, "w")
        
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        
    def flush(self):
        pass
        
sys.stdout = Logger("test06_target_file.txt")

print "This is a test for print output to a target file."
