#coding=utf-8

from sys import argv

script, filename = argv

print "We're going to open the file %r and input the Sound Level for calculate." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# 从命令行打开音级文件，如没有该文件，则创建之。
target = open(filename,'w+')

print "现在输入一行待计算的数字，每行的数字以空格间隔.", "\n"

# 从命令行输入几行待计算的音级，英文数字，以空格分隔
Level_1 = raw_input("Sound Level 1: ")

print "\nWe are goint to write these to the file Level.txt."
print "输入完毕，现在写入并关闭文件。\n"

# 向打开的文件中写入刚才输入的一行音级
target.write(Level_1)
target.write("\n")

target.close()

# 将输入的音级数字，转换为List，并按照从小到大排列。
def linelist(file):
    with open(file, 'r') as f:
        for line in f.readlines():
            # Python strip() 删除每行前后的空格
            linestr = line.strip() 
            
            # split() split() 通过指定分隔符对字符串进行切片存为List，此处默认用空格分隔
            linestrlist = linestr.split( ) 

            # map() 会根据提供的函数对指定序列做映射，最终将每一行列表中的字符转换为数值 
            linelist = map(int, linestrlist)
            
            # print "音级数：", len(linelist)
            
            linelist.sort(reverse = False);
            print "函数内序列0:音级从小到大排列:", linelist
    return linelist

#赋值给全局变量
soundlist = linelist(filename)

# 运行函数，显示列表中从小到大排列的音级


# print "函数外取值：", linelist


