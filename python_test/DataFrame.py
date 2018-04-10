from pandas import Series
import collections


def getMax(dic):
    dicList = (sorted(dic.items(), key=lambda item: item[1], reverse=True))
    mun = dicList[0][1]
    lis2 = []
    for item in dicList:
        num1 = item[1]
        if num1 < mun:
            break
        lis2.append(item)
    return lis2


columns1 = Series([
    '电影1', '电影2', '电影3', '电影4', '电影5', '电影6', '电影7', '电影8', '电影9', '电影10',
    '电影11', '电影12', '电影13', '电影14', '电影15'
])
columns2 = Series([
    '导演1', '导演2', '导演3', '导演1', '导演2', '导演3', '导演4', '导演1', '导演2', '导演3',
    '导演1', '导演2', '导演3', '导演4', '导演5'
])
columns3 = Series([
    ['演员1', '演员2', '演员3', '演员4'],
    ['演员3', '演员2', '演员4', '演员5'],
    ['演员1', '演员5', '演员3', '演员6'],
    ['演员1', '演员4', '演员3', '演员7'],
    ['演员1', '演员2', '演员3', '演员8'],
    ['演员5', '演员7', '演员3', '演员9'],
    ['演员1', '演员4', '演员6', '演员7'],
    ['演员1', '演员4', '演员3', '演员8'],
    ['演员5', '演员4', '演员3', '演员9'],
    ['演员1', '演员4', '演员5', '演员10'],
    ['演员1', '演员4', '演员3', '演员11'],
    ['演员7', '演员4', '演员9', '演员12'],
    ['演员1', '演员7', '演员3', '演员13'],
    ['演员10', '演员4', '演员9', '演员14'],
    ['演员1', '演员8', '演员11', '演员15'],
])
# datas = {'电影名称': columns1, '导演': columns2, '主要演员': columns3}
# films = DataFrame(data=datas, columns=['电影名称', '导演', '主要演员'])
print("\n电影最多的导演:([导演名]\\[电影个数])\n", getMax(collections.Counter(columns2)))

print("\n电影最多的演员:([演员名]\\[电影个数])\n",
      getMax(collections.Counter([i for item in columns3 for i in item])))
li = []
actorsX2 = [("演员" + item, "演员" + jitem) for item in map(str, range(1, 17))
            for jitem in map(str, range(int(item) + 1, 17))]
for item in actorsX2:
    for c in columns3:
        temp = list(set(item).intersection(set(c)))
        if len(temp) == 2:
            li.append(temp)
print("\n电影最多的演员组合:([演员名]\\[电影个数])\n",
      getMax(collections.Counter([i[0] + "和" + i[1] for i in li])))

# dict2 = collections.Counter(columns3.list)
