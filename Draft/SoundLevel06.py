#coding=utf-8

import sys

# 运行本程序时，不再需要跟输入的文本文件名。
# 实现了连续计算多个输入音级序列的音级排序。
# 定义程序保存运行结果的文件名为 sound_level_calc.txt，每次程序运行的结果，会自动添加到文件末尾。
# 程序开始后，输入end, exit, quit 退出执行。

# 以下代码实现同时在屏幕打印输出，同时将程序输出结果保存到 sound_level_calc.txt 文件中。
# 避免了单纯调用 sys 模块的 stdout 将输出重定向到文件的弱点（屏幕无输出）。
# 定义程序保存运行结果的文件名为 sound_level_calc.txt，每次程序运行的结果，会自动保存到文件末尾。

class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN, "a+")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

sys.stdout = Logger("sound_level_calc.txt")


# 开局指定一个循环，限定在输入值为 end, exit, quit 之外的情况下，持续执行音级计算。
# 注意，python 非常注重每行的缩进，在 while 循环之下的程序，都必须缩进四个空格。
while True:

	print "----(@^_^@)---现在输入一行待计算的音级，以空格间隔。---(*^_^*)----", "\n"

	# 从命令行输入一行待计算的音级，英文数字，以空格分隔
	level_1 = raw_input("以空格分隔的音级: ")

        if level_1.strip() == 'end':
            break

        elif level_1.strip() == 'exit':
            break

        elif level_1.strip() == 'quit':
            break



	# 将输入的音级数字，转换为List，并按照从小到大排列。
	def linelist(inputnum):
		"将键盘输入的数字行转换为从小到大排列的list"
		# Python strip() 删除每行前后的空格
		linestr = inputnum.strip()

		# split() split() 通过指定分隔符对字符串进行切片存为List，此处默认用空格分隔
		linestrlist = linestr.split( )

		# map() 会根据提供的函数对指定序列做映射，最终将每一行列表中的字符转换为数值
		linelist = map(int, linestrlist)

		# 将该列表从小到大排列
		linelist.sort(reverse = False);

		# 返回函数变量 linelist
		return linelist

	# 引用键盘输入变量 level_1 运行函数，显示列表中从小到大排列的音级
	soundlist = linelist(level_1)


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
	calc_diff(soundlist);


	def list_shift1(shiftlist, k):
		"转换初始音级的序列，将第一个音级放到序列尾端"

		mylength = len(shiftlist)
		if mylength != 0:

			#取列表的第k位起到最后一位，在后面加上被舍弃的位数
			shiftlist[:] = shiftlist[k:mylength] + shiftlist[0:k]

	print "\n"


	# 计算初始音级的 List 长度
	listnum = len(soundlist)

	# 创建一个从 1 开始，以 1 递增的列表，用以下列循环
	shiftnum = range(1,listnum)


	# 每次执行list_shift1，都会将原有音级的顺序向后推一个，所以执行次数为音级数；
	# 注意此时soundlist 每执行一次，原有顺序都会调整一格，所以不必要再调整 list_shift1函数的k值
	# 执行次数为上述定义的列表 shiftnum 的次数。
	for number in shiftnum:
		list_shift1(soundlist, 1)

		# 判断倒数第二个音～第一个音之间的音程
		if soundlist[len(soundlist)-2] >= soundlist[0]:
			temp2 = soundlist[len(soundlist) - 2] - soundlist[0]
		else:
			temp2 = soundlist[len(soundlist) - 2] +12 - soundlist[0]
	#    print temp2

	#    print "第 x 次转换的排序：", soundlist, "音程为：", temp2, "\n"
		print "第 %r 次转换的排序：" %number, soundlist, "音程为：", temp2, "\n"
