#-*- coding: utf-8 -*-

# r = 4 > 2 ** 4 or True is 1 and '4' in "345"
# r1 = 4 > 2 ** 4 or True is 1 and '4' in "345"
# print('r1', r)
# if r:
#     print('猜猜我的结果', r)
# else:
#     print('猜猜我的结果2', r)

# a = input("请输入 a：")
# b = input("请输入 b：")
# max_number = a if a > b else b
# print(max_number)
# 1. 定义一个计数器变量，从数字 1 开始，循环会比较方便
row = 1

while row <= 5:
    print("8" * row)

    row += 1


'''
可以看到，返回方式是 -> 
定义变量则要多加一个：在数据类型和变量名中间
这个时候有意思的来了，即便我不返回str类型，也没有问题
'''
def cs() -> str:
    str: zzz = '100'
    return 100