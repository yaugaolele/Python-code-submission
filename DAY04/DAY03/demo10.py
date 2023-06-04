# 字符串的下标
'''
    下标又叫做索引，就是编号。
'''
# name = "hoiaho"
# print(name[0])
# print(name[1])
# print(name[3])
# print(name[4])
# print(name[5])
# 注意防止数组下标越界


# 切片
'''
    切片是指对操作的对象其中一部分的操作，字符串、列表、元组都支持切片的操作。
    语法：
        序列[开始位置的下标：结束位置的下标：步长]
    注意：
        1.不包含结束位置下标对应的数据，正负整数都可以。
        2.步长是选取间隔，正负整数均可，默认步长为1
'''
name = "hshecoijoca"
print(name[0:4:1])
print(name[2:5])    # 省略步长

print(name[:5])     # 省略了开始与步长，默认开始位置为0  hshec
print(name[1:])     # 省略了结束与步长，默认是到最后一个结束   shecoijoca
print(name[:])      # 全部都省略，默认截取全部 hshecoijoca
print(name[::2])    # 只给步长，默认是截取全部步长为2   hhcioa
print(name[:-1])   # -1表示倒数的第一个数据
print(name[-4:-1])  # 表示到着从1到4
print(name[::-1])   # 步长为-1表示字符串反转
