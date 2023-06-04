'''
子类中调用父类同名的方法和属性
'''
class A(object):
    def __init__(self):
        self.a = 10

    def print_All(self):
        print(f"a的值为：{self.a}")


class B(object):
    def __init__(self):
        self.a = 20

    def print_All(self):
        print(f"a的值为：{self.a}")


class AB(A, B):
    # 子类重写父类同名方法和属性，默认使用子类的同名方法和属性
    def __init__(self):
        self.a = 30

    def print_All(self):
        # 如果先调用父类的属性和方法，父类属性会先覆盖子类属性，故在调用属性前，先调用自己子类初始化方法
        self.__init__()
        print(f"子类自己a的值为：{self.a}")

    # 调用父类方法，但是为保证调用到的属性也是父类的属性，必须在调用方法前调用父类的初始化
    def print_A(self):
        A.__init__(self)
        A.print_All(self)
    def print_B(self):
        B.__init__(self)
        B.print_All(self)

ab = AB()
ab.print_All()  # 子类自己a的值为：30
ab.print_A()    # a的值为：10
ab.print_B()    # a的值为：20
