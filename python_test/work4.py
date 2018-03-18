"""比赛评分：校园歌手大奖赛中，每个歌手的得分由10名评委和观众决定，
最终得分的规则是去掉10名评委所打分数的一个最高分和一个最低分，
再加上所有观众评委分数后的 '平均值'。
程序输入选手的10个评委分数和  观众评分(?)，
计算其最后得分
"""
gread = []
for i in range(1, 11):
    gread.append(int(input("please input your grade {}: ".format(i))))
gread.sort()
gread[0] = int(input("please input gerad :"))
gread.pop()
print("your gread is :%d" % (sum(gread) / len(gread)))
