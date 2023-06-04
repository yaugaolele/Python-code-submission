'''
    集合常见的操作方法
'''
# 添加数据 add()
s1 = {10, 20}
s1.add(30)
s1.add(40)
print(s1)   # {40, 10, 20, 30}
# 注意由于集合有去重功能，所以当向集合内追加数据，追加的数据是当前集合中存在的数据则不进行任何操作
s1.add(20)
print(s1)   # {40, 10, 20, 30}

# update()追加的数据是序列
s2 = {10, 20, 30}
# s2.update(40)
# print(s2)   # TypeError: 'int' object is not iterable
s2.update([100, 200])
print(s2)   # {100, 200, 10, 20, 30}
s2.update("abs", "adsc")
print(s2)   # {100, 200, 10, 'b', 20, 'c', 's', 'd', 30, 'a'}

# 删除数据 remove() 删除集合中的指定数据，如果数据不存在则报错
s3 = {10, 20, 30, 40, 50}
s3.remove(20)
print(s3)   # {50, 40, 10, 30}
# s3.remove(60)
# print(s3)   # KeyError: 60 数据不存在就会报错

# 删除数据 discard() 删除集合中的指定数据，如果数据不存在也不会报错
s3.discard(90)
print(s3)
s3.discard(30)
print(s3)   # {50, 40, 10}

# pop() 随机删除集合中的某个数据，并返回删除的这个数据
print(s3.pop())     # 50
print(s3)   # {40, 10}

# 查找数据
# in 判断数据在集合内
# not in 判断数据不在集合内

s4 = {100, 200, 10, 'b', 20, 'c', 's', 'd', 30, 'a'}
print(10 in s4)  # True
print(20 not in s4)     # False
