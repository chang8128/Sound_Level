#coding=utf-8

# 运行 python SoundLevel02.py level_input.txt 以计算音级
# 运行命令时输入的音级文本文件 level_input.txt 可以另起其他文件名。
# 本程序仅仅实现了在输入的文本文件的行内对数字进行排序，且没有回写到这个打开的文件内。
# 本程序实现了计算文本文件提供的多个音级的数字差。

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
# Level_2 = raw_input("Sound Level 2: ")
# Level_3 = raw_input("Sound Level 3: ")

print "\nWe are goint to write these to the file Level.txt."
print "输入完毕，现在写入并关闭文件。\n"

# 向打开的文件中写入刚才输入的三行音级
target.write(Level_1)
target.write("\n")
# target.write(Level_2)
# target.write("\n")
# target.write(Level_3)
# target.write("\n")

target.close()

# txt = open(filename)

# print "Here's your file %r: \n" % filename
# print txt.read()

# 从之前保存的文件中顺序读取每行以空格分隔的音级数字，并转换为List，再按照从小到大排列。
def readfile(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            # Python strip() 删除每行前后的空格
            linestr = line.strip() 
            # print linestr
            
            # split() split() 通过指定分隔符对字符串进行切片存为List，此处默认用空格分隔
            linestrlist = linestr.split( ) 
            #print linestrlist

            # map() 会根据提供的函数对指定序列做映射，最终将每一行列表中的字符转换为数值 
            linelist = map(int, linestrlist)
            print linelist
            
            print "音级数：", len(linelist)
            
            linelist.sort(reverse = False);
            print "序列0:音级从大到小排列:", linelist
            
#            min = linelist[0] #令min变量记录该列表中最大的值
#            for i in range( len(linelist) -1 ): #i用来控制列表下标, 元素个数-1为了防止下面的相减越界
#                if linelist[i] - linelist[i+1] < min: #当前一个数减后一个小于当前min里的值时, 更新最小值
#                    min = linelist[i] - linelist[i+1]
#            print "\n"
#            print "最小音级差为：", min
            
            
            min = linelist[len(linelist) -1] #令min为音级列表中的最大值
            max_diff = linelist[len(linelist) -1] - linelist[0] # 令max_diff变量记录该列表中最大的音级差
            print "\n最大音级 - 最小音级：", max_diff, "\n"
                        
            for j in range(len(linelist) -1):
                temp1 = linelist[j] + 12 - linelist[j+1]
                if temp1 < max_diff:
                    max_diff = temp1
                print "\n 第 %r 次循环的音级差、最小音级差分别为：" %j, temp1, "--", max_diff, "\n"
                                            
readfile(filename)


def list_shift1(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            # Python strip() 删除每行前后的空格
            linestr = line.strip() 
            
            # split() split() 通过指定分隔符对字符串进行切片存为List，此处默认用空格分隔
            linestrlist = linestr.split( ) 

            # map() 会根据提供的函数对指定序列做映射，最终将每一行列表中的字符转换为数值 
            linelist = map(int, linestrlist)
            
            #将列表按照从小到大的顺序排列 
            linelist.sort(reverse = False);
            
            #将列表的第一位数字插入到最后一位
            linelist.insert(len(linelist),linelist[0])
            
            #删除列表的第一位
            linelist_shift1 = linelist.pop(0)
            print "序列1的音级为：", linelist

            

list_shift1(filename)




