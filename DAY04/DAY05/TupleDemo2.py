'''
    元组的常见操作: 元组数据不支持修改，只支持查找
'''
# 按下标查找数据
tuple1 = ("aa", "bb", "cc", "dd", "bb")
print(tuple1[0])

# index()：查找某个数据，如果数据存在则返回对应的下标，不存在返回报错，语法与列表、字符串的index方法相同
print(tuple1.index("aa"))
# print(tuple1.index("bbb"))  # ValueError: tuple.index(x): x not in tuple

# count():统计某个数据在当前元组中出现的次数
print(tuple1.count("bb"))

# len(): 统计元组中的数据的个数
print(len(tuple1))

# 注意元组内的直接数据如果修改则立即报错
# tuple1[0] = "jjj"   # TypeError: 'tuple' object does not support item assignment

# 但是如果元组中有列表，修改列表中的数据是支持的
tuple2 = ("aa", "bb", "cc", "dd", "bb", [10, 20, 30])
print(tuple2[5])
tuple2[5][2] = 40   # 修改元组中列表的数据
print(tuple2)   # ('aa', 'bb', 'cc', 'dd', 'bb', [10, 20, 40])


