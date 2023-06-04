'''
    函数的参数
'''
# 1.位置参数：调用函数时根据函数定义的参数位置来传递参数
def user_info(name, age, sex):
    print(f"您的名字：{name},您的年龄：{age},您的性别：{sex}")

user_info('Tom', 18, '男')   # 您的名字：Tom,您的年龄：18,您的性别：男
# 传递和定义参数的顺序及个数要保持一致

# 2. 关键字参数 函数调用时通过“键 = 值”形式加以指定，可以让函数更加清晰，容易使用，同时也清除了参数的顺序问题

def user_info(name, age, sex):
    print(f"您的名字：{name},您的年龄：{age},您的性别：{sex}")
user_info("Tom", age=18, sex='女')
user_info("Rose", sex='男', age=20)
# user_info(sex='男', age=20,"Rose") # 编译错误

# 注意函数调用时，如果有位置参数时，位置参数必须在关键字的前面，但关键字参数之前不存在先后顺序

'''
3.缺省参数：
    也叫默认参数，用于定义函数，为参数提供默认值，调用函数时，可以不传默认参数值
    注意：
    所有位置参数必须出现在默认参数前，包括函数的定义和调用
'''
# def user_info(name, age = 18, sex):
def user_info(name, age = 18, sex = '男'):
    print(f"您的名字：{name},您的年龄：{age},您的性别：{sex}")

user_info("Rose", 20, '男')

'''
4.不定长参数
不定长参数也可叫做可变参数，用于不确定调用的时候会传递多少个参数（不传参也可以）的场景
此时，可以包裹(packing)位置参数，或者包裹关键字参数，来进行参数传递，会显得非常方便
'''
def user_info(**kwargs):
    print(kwargs)

user_info(name="Tom")
user_info(name="Tom", age=19, sex='男')  # {'name': 'Tom', 'age': 19, 'sex': '男'}
# 注意：无论包裹位置传递，还是包裹关键字传递都是一个组包的过程





