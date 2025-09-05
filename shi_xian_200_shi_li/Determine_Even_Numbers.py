#-*- coding: utf-8 -*-
#4	判断一个数是否是偶数

num=input("输入一个数：")
try:
    float(num)  # 尝试转换为浮点数
    if '.' in num: #检查是不是小数 s.replace('.', '', 1).isdigit() 检测数字字符（包括浮点数）
        num=input("请输入整数")
    if '-' in num: #检查是不是负数s.replace('-', '', 1).replace('.', '', 1).isdigit() and s.count('-') <= 1
        num=input("请输入正整数")
    if int(num)%2 == 0 : #s.isdigit() 只能检测正整数
        print("这是个偶数")
    if int(num)%2 != 0 : 
        print("这是个奇数数")
except ValueError:
    print("这不是数字")

