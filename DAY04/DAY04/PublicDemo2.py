'''
    公共方法
'''
'''
    函数      描述
    len()     计算容器元素中的个数
    min()     返回容器中元素中的最小值
    range()   生成从start到end
'''
# len()
# 1.字符串
str1 = "adas "
print(len(str1))

# 2.列表
list1 = [10, 20, 30, 40]
print(len(list1))

# 3.元组
t1 = (1, 2, 3, 4, 5)
print(len(t1))

# 4.集合
s1 = {10, 20, 30, 40}
print(len(s1))

# 5.字典
dict1 = {"name": "Tom", "age": 19}
print(len(dict1))

# del / del()
str1 = "asjxiax"
del str1
# print(str1)    # NameError: name 'str1' is not defined

# 2.列表
list1 = [10, 20, 30, 40]
del(list1[0])
print(list1)

# max min
# 1.字符串
str1 = "scoasicnoas"
print(max(str1))    # 使用ASCII码值排序
print(min(str1))

# 2.列表
list1 = [10, 20, 30, 40]
print(max(str1))
print(min(str1))

# 3.range()
for i in range(1, 10, 1):
    print(i, end=" ")   # 1 2 3 4 5 6 7 8 9 含头不含尾

print()
for i in range(10):
    print(i, end=" ")   # 0 1 2 3 4 5 6 7 8 9

# 注意：range()生产的序列不包含end数字

# enumerate()
# 语法：enumerate(可遍历对象，start = 0)
# 注意： start参数用来设置遍历数据下标的起始值，默认为0
list1 = ["a", "b", "c", "e"]
for i in enumerate(list1):
    print(i)

for index, char in enumerate(list1, start=1):
    print(f"下标是{index},对应的字符是{char}")

