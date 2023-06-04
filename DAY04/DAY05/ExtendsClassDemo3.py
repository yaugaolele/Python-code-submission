'''
多继承
    就是一个类同时继承了多个父类
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
        print(f"a的值为：{self.a}")

ab = AB()
print(ab.a)
print(ab.a)     # 当一个类有多个父类时，默认使用第一个父类的同名方法和属性
ab.print_All()

