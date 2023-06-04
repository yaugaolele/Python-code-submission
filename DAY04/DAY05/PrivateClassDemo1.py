'''
    定义私有权限(属性和方法)
    在Python中可以把实例属性和方法设置私有权限，即设置某个实例属性或实例方法不继承给子类
    设置私有权限的方法：在属性名和方法名前面加上两个下划线__
'''
class Person(object):
    def __init__(self):
        self.name = "李四"
        self.age = 18
        self.__sex = "男"

    # 获取私有属性
    def get_sex(self):
        return self.__sex

    # 修改私有属性的方法
    def set_sex(self):
        self.__sex = "女"

    def print_info(self):
        print(f"姓名为{self.name},年龄为{self.age}")

class Student(Person):
    def __init__(self):
        self.name = "张三"
        self.age = 20
        # 设置私有属性
        self.__id = 123456


    # 获取私有属性
    def get_id(self):
        return self.__id

    # 修改私有属性的方法
    def set_id(self):
        self.__id = "女"

    def print_info(self):
        self.__init__()
        print(f"姓名为{self.name},年龄为{self.age}")

    # 定义私有方法
    def __info_print(self):
        print(self.__id)
        print(self.name)
        print(self.age)

s = Student()
s.print_info()
# s.__info_print()    # AttributeError: 'Student' object has no attribute '__info_print'
# 对象无法访问私有属性和私有方法
# print(s.__sex) # 子类无法继承父类的私有属性和私有方法

'''
    获取和修改私有属性值
    在Python中一般定义函数名get_XX用来获取私有属性，定义set_XX来修改私有属性
'''

p = Person()
print(p.get_sex())  # 男
p.set_sex()
print(p.get_sex())  # 女


