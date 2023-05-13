# 数据类型的转换
# 转换函数
'''
    int(x[, base]) 将x转换为一个整数
    float(x)  将x转换为一个浮点数
    str(x)  将对象x转换为一个字符串
    eval(str)  用来计算字符串中的有效Python表达式，并返回一个对象
    tuple(s)   将序列s转为一个元组
    list(s)  将序列s转为一个列表
    char(x)  将一个整数转为Unicode字符
    ord(x)  将一个字符转为它所对应的ASCII整数
    hex(x)  将整数转为十六进制
    oct(x)  将整数转为八进制
    bin(x)  将整数转为二进制
'''

# 1.接收用户的输入
num = input("请输入您的幸运数字：")


# 2.打印结果
print(f"您的幸运数字是：{num}")

# 3.检测接收到用户输入的数据类型
print(type(num))  # <class 'str'>

# 4.类型转换 : 转换数据类型为整数类型
print(type(int(num)))  # <class 'int'>

a = 20013
print(chr(a))   # 20013 转为Unicode为汉字“中”
b = 12
print(hex(b))   # 12 的十六进制表示 0xc
c = 8
print(bin(c))   # 8 的二进制为0b1000









