# 字符串
'''
    字符串Python中最常用的数据类型，我们一般使用引号来创建字符串，创建字符串很简单只要为变量分配一个值即可。
    注意：
    三引号形式的字符串支持换行
'''
a = "Jerry"
b = 'ncosndc'
c = """
    I love me
"""
print(c)
e = '''
    Hello World
'''

# 字符串输出
print("hello world")
name = "tomorrow"
print("我的名字是：%s" % name)
print(f"我的名字是：{name}")

# 字符串输入
# 在Python中使用input()接收用户的输入
name = input("请输入你的名字：")
print(f"您输入的名字是{name}")
print(type(name)) # <class 'str'>

age = input("请输入您的年龄：")
print(f"您输入的年龄是{age}")
print(type(age))    # <class 'str'>