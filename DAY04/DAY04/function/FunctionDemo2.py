'''
    函数的参数作用
'''
# 定义函数的同时定义了接收用户数据的参数a 和 b，a 和 b是形参
def add_num1():
    result = 1 + 2
    print(result)

add_num1()

def add_num2(a, b):  # 形参
    result = a + b
    print(result)

add_num2(2, 3)  # 实参
#
# # 函数返回值的作用
# # 在函数中如果需要返回结果给用户需要返回值
def buy():
    return "好吃滴！！！"
# 使用变量来保存函数的返回值
goods = buy()
print(goods)


'''
    应用：制作一个计算器，计算任意俩数字之和，并保留
'''
def sum_num(a, b):
    return a + b

a = int(input("请输入第一个数字："))
b = int(input("请输入第二个数字："))
result = sum_num(a, b)
print(f"两数之和为：{result}")

'''
    函数的说明文档
    文档注释
'''
# 定义一个函数的说明文档
'''
    def 函数名(参数):
        """说明文档的位置"""
        代码
        .......
查看函数说明
help(函数名)
'''
def sum_num(a, b, c):
    """求三个数之和的函数"""
    return a + b + c
help(sum_num)

'''
    函数的嵌套调用
    所谓函数嵌套调用指的是一个函数里面又调用了另一个函数
'''

def teatA():
    print("hello")

def testB():
    teatA()
    print("world")

testB()

'''
课堂练习：
1. 编写函数求三个数之和
2. 编写函数求三个数的平均值
'''
# 1
def sum_num(a, b, c):
    return a + b + c

# 2
def avg_num(a, b, c):
    return sum_num(a, b, c) / 3

a = int(input("请输入第一个数字："))
b = int(input("请输入第二个数字："))
c = int(input("请输入第三个数字："))
sum = sum_num(a, b, c)
print(f"三个数字的和是：{sum}")
avg = avg_num(a, b, c)
print(f"三个数字的平均值是：{avg}")
