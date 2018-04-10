# # 求1000以内素数
# import math
import numpy as np
import matplotlib.pyplot as pt

# def isPrime(n):
#     for j in range(2, int(math.sqrt(n)) + 1):
#         if n % j == 0:
#             return False
#     return True

# priNum = [2]
# sum = 2
# for i in range(3, 1000):
#     if isPrime(i):
#         sum += i
#         priNum.append(i)
# print("1000以内的素数和为：%d" % (sum))
# print(priNum)

print("+++++++++++++房价预测++++++++++++")
x, y = [], []
for sample in open("f:\\Workspace\\VSCWorkspace\\python_test\\prices.txt",
                   'r'):
    _x, _y = sample.split(",")
    x.append(float(_x))
    y.append(float(_y))
x, y = np.array(x), np.array(y)
x = (x - x.mean()) / x.std()
pt.figure()
# pt.scatter(x, y, c='g', s=6)
# pt.show()
x0 = np.linspace(-2, 4, 100)


def get_model(deg):
    return lambda input_x=x0: np.polyval(np.polyfit(x, y, deg), input_x)


def get_cost(deg, input_x, input_y):
    return 0.5 * ((get_model(deg)(input_x) - input_y)**2).sum()


test_set = (1, 4, 10)
for d in test_set:
    print(get_cost(d, x, y))
pt.scatter(x, y, c='g', s=20)
for d in test_set:
    pt.plot(x0, get_model(d)(), label="degree={}".format(d))
pt.xlim(-2, 4)
pt.ylim(1e5, 8e5)
pt.legend()
pt.show()
