#-*- coding: utf-8 -*-
#5	判断一个数是否是质数
import math

num=input("输入一个数：")
try:
    float(num)  # 尝试转换为浮点数
    if '.' in num: #检查是不是小数 s.replace('.', '', 1).isdigit() 检测数字字符（包括浮点数）
        num=input("请输入整数")
    if '-' in num: #检查是不是负数s.replace('-', '', 1).replace('.', '', 1).isdigit() and s.count('-') <= 1
        num=input("请输入正整数")
    if int(num) == 0:
        num=input("请输入非0的正整数")
    if (int(num)%2 == 0 and int(num) !=3) or(int(num)%3 == 0 and int(num) !=3): 
        #s.isdigit() 只能检测正整数
        print("这是个能被2或3整除的数（非2或3）")
    if (int(num)%2 != 0 and int(num)%3 != 0) or int(num) == 2 or int(num) == 3:  
        n = int(num)
        c:bool
        # # 牛顿迭代法
        # x = n
        # y = (x + 1) // 2
        # while y < x:
        #     x = y
        #     y = (x + n // x) // 2
        
        # print(x)
        # print(math.isqrt(n))
        # if x<0:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                c = False
            else:
                c = True

        if c :
            print("这是质数")
        else:
            print("这不是质数")
        
    #蒜了蒜了，写不出来，质数这玩意，我这辈子都用不上
except ValueError:
    print("这不是数字")

