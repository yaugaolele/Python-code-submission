'''
    变量的作用域：
        变量的作用域指的是变量的生效范围，主要发为两类：局部变量和全局变量
    局部变量：
        所谓局部变量是定义在函数内部的变量，即只在函数内部生效
'''
def testA():
     a = 100
     print(a)

testA()
# print(a)
# 局部变量的作用在函数体内部临时保存数据，当出函数体的时候就会销毁变量

'''
全局变量
    指的是在函数体内外都可以生效的变量
'''
# 定义一个全局变量
b = 200
def testB():
    print(b)    # 访问全局变量并打印b存储的数据

def testC():
    print(b)
testB()
testC()
print(b)

a = 100
def testB1():
    a = 10
    print(a)
testB1()
# 在函数体内部修改全局变量的值

c = 100
def test01():
    print(c)

def test02():
    # global 关键字声明c是全局变量
    global c
    c = 200
    print(c)

test01()
test02()
print(c)


