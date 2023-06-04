'''
    魔法方法
        在Python中，__XX__ () 的函数叫做魔法方法，指的是具有特殊功能的哈函数
        注意：
            __init__()的方法，在创建的时候默认被调用，不需要手动调用
            __init__(self)中的self，不需要开发者传递，Python解释器会自动把当前的对象引用
'''
# __init__() 方法的作用：初始化对象
class Person():
    # 初始化功能的函数
    def __init__(self):
        # 添加实例shuxinn
        self.name = "李四"
        self.age = 19
    # 普通函数
    def print_info(self):
        # 在类里面调用实例属性
        print(f"学生的姓名：{self.name}")
        print(f"学生的姓名：{self.age}")
# 创建对象
# 学生的姓名：李四
# 学生的姓名：19
p = Person()
p.print_info()

p2 = Person()
p2.print_info()
print("==================")

# 带参数的__init__()函数，
class Student():
    # 初始化功能的函数
    def __init__(self, name, age):
        # 添加实例shuxinn
        self.name = name
        self.age = age
    # 普通函数
    def print_info(self):
        # 在类里面调用实例属性
        print(f"学生的姓名：{self.name}")
        print(f"学生的姓名：{self.age}")

s = Student("王五",20)
s.print_info()
# 学生的姓名：王五
# 学生的姓名：20