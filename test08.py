# -*- coding: UTF-8 -*-

print("这是阶乘计算器. -1 to stop.")
n = int(input("阶乘: "))

while n >= 0:    
    prod = 1    
    for i in range(2, n + 1):        
        prod = prod * i    
        
    print("阶乘", n, "is", prod)
    
#n!    
    n = int(input("这是阶乘计算器: "))
    
print("Bye!")

