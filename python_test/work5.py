import re
import collections
# coding=gbk
# utf-8格式读取文件到str
f = open(
    "f:\\Workspace\\VSCode Workspace\\python_test\\text.txt",
    "r",
    encoding="utf-8")
str1 = f.read()
# 利用正则表达式去掉所有标点，利用\pP无法实现正则匹配（貌似）
slist = re.split('\\s|/|:|\\(|\\)|,|\\.|/|\"|\\*|\\ufeff', str1)
# 去掉list中的全部空项，必须要用到while（貌似）仅slist.remove('')list将none，还不知道为什么会产生空项。。。
while '' in slist:
    slist.remove('')
# 利用collections.Counter()统计列表中的词频，返回为‘单词“：‘词频’格式的字典
Dic = dict(collections.Counter(slist))
''' 利用sorted函数对字典元素进行排序，
利用items()函数酱Dic转化为可迭代对象
再利用lambda函数选择迭代对象的第二项（单词词频）进行比较排序'''
dic = sorted(Dic.items(), key=lambda item: item[1], reverse=True)
for i in range(0, len(dic)):
    print("第%-5d个  %s" % (i + 1, dic[i][0]))
