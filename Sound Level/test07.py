#coding=utf-8

# 八皇后问题

"""
def queen(A, cur=0):
	if cur == len(A):
		print(A)
		return 0
	for col in range(len(A)):
		A[cur], flag = col, True
		for row in range(cur):
			if A[row] == col or abs(col - A[row]) == cur - row:
				flag = False
				break
		if flag:
			queen(A, cur+1)
queen([None]*8)
"""

'''
while True:
    m = input("输入年纪")
    if m> 18:
        break
'''

while True:
        
	print "现在输入一行待计算的音级，以空格间隔。", "\n"

	# 从命令行输入一行待计算的音级，英文数字，以空格分隔
	level_1 = raw_input("以空格分隔的音级: ")

        if level_1.strip() == 'end':
            break