from math import *
# 3个参数的输入
a = int(input("二次项系数："))
b = int(input("一次项系数："))
c = int(input("常数项系数："))
d = b**2 - 4*a*c
if d < 0:
    print("此二次方程无实数根")
elif d == 0:
    outcome = -b/(2*a)
    print("方程有且仅有一个实数根：%d" % outcome)
elif d > 0 :
    x1 = (-b + sqrt(d))/(2*a)
    x2 = (-b - sqrt(d))/(2*a)
    print("方程有两个实数根，分别为：%d和%d" % (x1, x2))
