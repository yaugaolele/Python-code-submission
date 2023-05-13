# 数据类型转换
# 1.float() --- 转换成浮点型
num1 = 1
print(float(num1))   # 1.0
print(type(float(num1))) # <class 'float'>

# 2.str() --- 转换为字符串类型
num2 = 10;
print(str(num2))
print(type(str(num2)))

# 3.tuple() --- 将一个序列转换为元组类型
list1 = [10, 20, 30]
print(tuple(list1))     # (10, 20, 30)
print(type(tuple(list1)))  # <class 'tuple'>

# 4.list() --- 将一个序列转换为列表
t1 = (100, 200, 300)
print(list(t1))     # [100, 200, 300]
print(type(list(t1)))   # <class 'list'>

# 5.eval() --- 将字符串中的数据转换成Python的表达式原本类型
str1 = "10"
str2 = "[1, 2, 3]"
str3 = "(10, 20, 30)"
print(eval(str1))   # 10
print(type(eval(str1)))  # <class 'int'>

print(eval(str2))   # [1, 2, 3]
print(type(eval(str2)))  # <class 'list'>

print(eval(str3))   # (10, 20, 30)
print(type(eval(str3)))   # <class 'tuple'>