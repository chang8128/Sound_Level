#coding=utf-8

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
        
sys.stdout = Logger("target_file.txt")

print "This is only a test"
