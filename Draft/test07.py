#coding=utf-8

# 测试一个循环输入音级的命令行，手动输入end停止。
while True:
        
	print "现在输入一行待计算的音级，以空格间隔。", "\n"

	# 从命令行输入一行待计算的音级，英文数字，以空格分隔
	level_1 = raw_input("以空格分隔的音级: ")

        if level_1.strip() == 'end':
            break
