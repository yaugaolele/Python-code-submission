'''
    当使用print输出对象的时候，默认打印对象的内存地址，如果类定义了__str__方法，那么就会打印从这个方法中的return的数据。

'''
class Student():
    # 初始化功能的函数
    def __init__(self, name, age):
        # 添加实例shuxinn
        self.name = name
        self.age = age
    # def __str__(self):
    #     return "这是一个学生类"
    def __del__(self):
        print(f"{self}对象已经被删除")
s = Student("张三",18)
print(s)    # 这是一个学生类
# 如果不写__str__默认打印内存地址,类似于java中的toSting方法

'''
    __del__()删除对象的时候,Python解释器也会调用该方法
'''
del s   # <__main__.Student object at 0x000001EFA09C1FD0>对象已经被删除

