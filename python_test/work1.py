''' 问题：a，b，c，d四人中有一名小偷，其中
    a:我不是，
    b:c是，
    c:肯定是d，
    d:c胡说，
其中仅一人说谎，用程序判断
解法：
设数组[0,0,0,0](0表示不是小偷，分别判断四种情况中满足abcd说法满足true=3的情况，这时数组中的1位小偷)
'''
res = ['a', 'b', 'c', 'd']
r = -1
for i in range(0, 4):
    sum = 0
    if i != 0:
        sum += 1
    if i == 2:
        sum += 1
    if i == 3:
        sum += 1
    if i != 3:
        sum += 1
    if sum == 3:
        r = i
print("小偷是=%c" % (res[r]))
