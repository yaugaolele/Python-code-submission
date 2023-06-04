# 循环
# while的语法
'''
    语法：
        while 条件：
            循环体
    循环三要素：
        1.循环的初始值
        2.循环的条件
        3.循环变量的改变
'''
# 输出 10 遍“人生苦短，我用Python”
i = 0
while i < 10:
    print("人生苦短，我用Python")
    i += 1
print("循环结束！")


# 利用while循环统计1 - 100 之间的累加和
i = 1
sum = 0
while i <= 100:
    sum += i    # 累加和
    i += 1  # 循环变量的改变
print(sum)

# 练习： 利用while循环计算1 - 100 之间的偶数和

# 方法一
j = 1
sum1 = 0
while j <= 100:
    if j % 2 == 0:
        sum1 += j
    j += 1
print(sum1)

# 方法二
i = 2
sum = 0
while i <= 100:
    sum += i
    i += 2
print(sum)

# while循环的嵌套
'''
    while 循环嵌套
    语法：
        while 条件1：
            语句1
            ...
            while 条件2：
                语句2
                ...
总结： 所谓while循环嵌套，就是一个while里面嵌套了一个while循环的写法，每个while循环的语法都是一样的
'''
j = 1
while j <= 3:
    i = 1
    while i <= 3:
        print("学习")
        i += 1
    print(f"学习的第{j}天")
    print(f"第{j}天的学习结束")
    j += 1
print("拿到offer！！！")
# 课堂练习：
'''
    用* 打印一个正方形
'''
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print(" * ", end="")
        j += 1
    print()
    i += 1

'''
    用* 打印一个三角形
'''
i = 1
while i <= 3:
    # 打印每一行的空格
    k = 1
    while k <= 3 - i:
        print(" ", end=" ")
        k += 1
    j = 1
    # 打印每一行的*
    while j <= (2 * i - 1):
        print("*", end=" ")
        j += 1
    print()
    i += 1

'''
    用循环完成9 * 9 乘法表
'''
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{i} * {j} = {i * j} ", end=" ")
        j += 1
    print()
    i += 1
# 课堂练习：
'''
    用* 打印一个正方形
'''
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print(" * ", end="")
        j += 1
    print()
    i += 1

'''
    用* 打印一个三角形
'''
i = 1
while i <= 3:
    # 打印每一行的空格
    k = 1
    while k <= 3 - i:
        print(" ", end=" ")
        k += 1
    j = 1
    # 打印每一行的*
    while j <= (2 * i - 1):
        print("*", end=" ")
        j += 1
    print()
    i += 1

'''
    用循环完成9 * 9 乘法表
'''
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{i} * {j} = {i * j} ", end=" ")
        j += 1
    print()
    i += 1
# for循环
'''
    语法：
        for 临时变量 in 序列：
            重复执行代码
            ......
'''
#
# 配合 break
# str = "yanandaxue"
# for i in str:
#     if i == 'd':
#         print("遇到d不打印")
#         break
#     print(i)

# 配合continue
str = "yananun"
for i in str:
    if i == 'u':
        print("遇到u不打印")
        continue
    print(i)
# 循环可以配合else使用，else下缩进的代码指定是当循环正常结束之后要执行的代码
'''
    语法：
        while 条件：
            重复执行代码1
        else：
            循环正常结束之后要执行的代码
'''
# i = 1
# while i <= 5:
#     print("努力学习！")
#     i += 1
# else:
#     print("最终拿到offer！")
# print("====================")
# 退出循环的方式
# break
# i = 1
# while i <= 5:
#     if i == 3:
#         print("没有好好上课！,回家卖红薯")
#         break
#     print("努力学习！")
#     i += 1
# else:
#     print("最终拿到offer！")

'''
    所谓else指的是循环正常结束之后要执行的代码，如果循环非正常结束（break）else下的代码就不执行了
'''
# print("====================")

# 退出循环的方式
# break
# i = 1
# while i <= 5:
#     if i == 3:
#         print("没有好好上课！")
#         i += 1
#         continue
#     print("努力学习！")
#     i += 1
# else:
#     print("最终拿到offer！")
'''
    因为continue是退出当前循环，继续执行下一次循环，所以该循环在continue控制下可以正常结束
'''

'''
     for 循环配合else
     语法：
        for临时变量 in 序列：
            重复执行的代码
        else:
            循环正常结束执行的代码
'''
# str = 'yandaxue'
# for i in str:
#     print(i)
# else:
#     print("循环正常结束")

# 退出方式
'''
    break:
'''
# str = "yanandaxue"
# for i in str:
#     if i == "u":
#         print("遇到U不打印")
#         break
#     print(i)
# else:
#     print("循环正常结束")

'''
    continue:
'''
str = "yanandaxue"
for i in str:
    if i == "u":
        print("遇到U不打印")
        continue
    print(i)
else:
    print("循环正常结束")

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
