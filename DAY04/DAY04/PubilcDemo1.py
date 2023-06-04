'''
    公共操作：
        运算符
        +：合并 支持字符串、列表、元组
        *：复制 支持字符串、列表、元组
        in：元素是否存在     支持字符串、列表、元组、字典
        not in：元素是否不存在    支持字符串、列表、元组、字典
'''

# +
str1 = "aa"
str2 = "bb"
str3 = str1 + str2
print(str3)     # aabb

# 列表
list1 = [1, 2]
list2 = [3, 4]
list3 = list1 + list2
print(list3)    # [1, 2, 3, 4]

# 元组
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)   # (1, 2, 3, 4)

# *复制
# 1.字符串
print("-" * 10)     # ----------

# 2.列表
list1 = [1]
print(list1 * 4)    # [1, 1, 1, 1]

# 3.元组
t1 = ("word")
print(t1 * 5)   # wordwordwordwordword

# in / not in
# 1.字符串
print("a" in "acai")    # True
print("e" in "sndo")    # False
print("a" not in "asdasc")   # False

# 2.列表
list1 = ['a', 'b', 'c', 'd']
print("a" in list1)
print("a" not in list1)

# 3.元组
t1 = ("a", "b", "c", "d")
print("aa" in t1)
print("aa" not in t1)

