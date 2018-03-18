'''猴子爬山：50级台阶，可跳1，2，3，
分析可知：台阶数   跳法数
            50      10,562,230,626,642
            20      121,415
            5       13
            4       7
            3       4
            2       2
于是。。。。
'''
""" print("star")
def fuc(x):
    if x>5:
        return fuc(x-1)+fuc(x-2)+fuc(x-3)
    elif x==5:
        return 13
    elif x==4:
        return 7
    elif x==3:
        return 4
num=fuc(20)
print("猴子有%d中跳法"%num)
print("end")
50会爆炸的递归，去死吧，不想用了
分析它的树形结构得知，当n＞3时，n级台阶的跳法＝(n-3)+(n-2)+(n-1)根据此构造算法。。。
 """
"""  def fuc(x):
     if x>5:
         fuc(x)
    elif x==5:
        return 13
    elif x==4:
        return 7
    elif x==3:
        return 4
num=fuc(20)
print("猴子有%d中跳法"%num)
print("end") """
x = int(input("请输入总阶数:"))
num = [0]
print("star")
for i in range(1, x + 1):
    if i > 3:
        num.append(num[i - 1] + num[i - 2] + num[i - 3])
    elif i == 3:
        num.append(4)
    elif i == 2:
        num.append(2)
    elif i == 1:
        num.append(1)
    print("%d %-20.f" % (i, num[i]))


print("台阶数为%d时，猴子有%d中跳法" % (x, num[x]))
print("end  ")
