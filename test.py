#-*- coding: utf-8 -*-

r = 4 > 2 ** 4 or True is 1 and '4' in "345"
r1 = 4 > 2 ** 4 or True is 1 and '4' in "345"
print('r1', r)
if r:
    print('猜猜我的结果', r)
else:
    print('猜猜我的结果2', r)
