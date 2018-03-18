# 求1000以内素数
import math


def isPrime(n):
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return False
    return True


priNum = [2]
sum = 2
for i in range(3, 1000):
    if isPrime(i):
        sum += i
        priNum.append(i)
print("1000以内的素数和为：%d" % (sum))
print(priNum)
