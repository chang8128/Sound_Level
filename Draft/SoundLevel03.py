#coding=utf-8

# 运行 python SoundLevel03.py level_input.txt 以计算音级
# 运行命令时输入的音级文本文件 level_input.txt 可以另起其他文件名。
# 仅实现了在输入的文本文件的行内对数字进行排序，且没有回写到这个打开的文件内。
# 实现了计算文本文件提供的多个音级的数字差，并计算x次排序的音程。

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

# 向打开的文件中写入刚才输入的三行音级
target.write(Level_1)
target.write("\n")

target.close()

# 从之前保存的文件中顺序读取每行以空格分隔的音级数字，并转换为List，再按照从小到大排列。
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
            #print "函数内序列0:音级从小到大排列:", linelist
    return linelist

#运行函数，显示列表中从小到大排列的音级
soundlist = linelist(filename)

print "函数外显示初始音级：", (soundlist)

            
def calc_diff(mylist):            
    "计算初始音级的音程"
    #令min为音级列表中的最大值
    min = mylist[len(mylist) -1] 
            
    #令max_diff变量记录该列表中最大的音级差
    max_diff = mylist[len(mylist) -1] - mylist[0] 
    print "\n最大音级 - 最小音级：", max_diff
                        
    for i in range(len(mylist) -1):
        temp1 = mylist[i] + 12 - mylist[i + 1]
        if temp1 < max_diff:
            max_diff = temp1
        print "\n 第 %r 次循环的音级差、最小音级差分别为：" %i, temp1, "--", max_diff


# 运行函数，显示函数 calc_diff 计算的音级差  
#calc_diff([0,4,8,9,11,12]) 测试用的list
calc_diff(soundlist);


def list_shift1(shiftlist, k):
    "转换初始音级的序列，将第一个音级放到序列尾端"
    
    mylength = len(shiftlist)    
    if mylength != 0:
        
        #取列表的第k位起到最后一位，在后面加上被舍弃的位数
        shiftlist[:] = shiftlist[k:mylength] + shiftlist[0:k]

print "\n"

# 每次执行list_shift1，都会将原有音级的顺序向后推一个，所以执行次数为音级数；
# 注意此时soundlist 每执行一次，原有顺序都会调整一格，所以不必要再调整 list_shift1函数的k值
for number in soundlist:
    list_shift1(soundlist, 1)

# 判断倒数第二个音～第一个音之间的音程    
    if soundlist[len(soundlist)-2] >= soundlist[0]:
        temp2 = soundlist[len(soundlist) - 2] - soundlist[0]
    else:
        temp2 = soundlist[len(soundlist) - 2] +12 - soundlist[0]
#    print temp2
    
    print "第 x 次转换的排序：", soundlist, "音程为：", temp2, "\n"



"""
#调用函数 list_shift1，移动的元素为一位
list_shift1(soundlist, 1);
print "第一次转换后的列表：", soundlist

#调用函数 list_shift1，移动的元素为两位
list_shift1(soundlist, 1);
print "第二次转换后的列表：", soundlist
"""

