sum = [0]


def checknum(i):
    sum[0] = i
    for i in range(0, 5):
        if sum[0] % 4 != 0:
            return False
        sum[0] = (sum[0] / 4) * 5 + 1
    if sum[0] % 5 != 0:
        return True
    else:
        return False


for i in range(1, 100001):
    if checknum(i):
        print("i=%d result=%d" % (i, int(sum[0])))
