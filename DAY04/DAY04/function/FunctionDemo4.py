'''
    多函数程序执行流程
'''
# 1.公用全局变量
# 定义一个全局变量
glo_num = 0
def test1():
    global glo_num
    # 修改全局变量
    glo_num = 100

def test2():
    # 调用test1()函数修改后的glo_num
    print(glo_num)  # 100

# 2. 调用test1函数，执行函数内部代码声明和修改全局变量
test1()
# 3. 调用test2函数执行函数内部代码
test2()

'''
    把返回值作为参数传递
'''
def test01():
    return 50
def test02(num):
    return num
# 1.保存test01函数的返回值
result = test01()
# 2.将test01的返回值作为参数传递给test02函数
print(test02(result))

'''
    函数的返回值
'''

def return_num():
    return 1
    return 2
# 如果函数中有两个return此时只执行第一个，因为return可以退出函数 导致return下方的代码就不执行了
result = return_num()
print(result)

def return_num2():
    return 1, 2

result1 = return_num2()
print(result1)  # (1, 2)
# 注意：return a, b 的写法 返回多个数据的时候默认是元组类型
# return 后面可以连接我们的列表、元组、字典以返回多个值

def return_num2():
    return [1, 2, 3]
result2 = return_num2()
print(result2)  # [1, 2, 3]

