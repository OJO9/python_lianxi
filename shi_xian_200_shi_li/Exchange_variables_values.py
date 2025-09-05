#-*- coding: utf-8 -*-
#3	交换两个变量的值
a:str = 'e'
b:str = 'mmm'

print("交换前"+a+b)

c:str = b
b=a
a=c

print("交换后"+a+b)
