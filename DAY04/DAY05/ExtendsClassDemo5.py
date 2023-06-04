'''
    多层继承

'''
class A(object):
    def __init__(self):
        self.num = 10

    def print_info(self):
        print(f"num的数值是：{self.num}")

class B(object):
    def __init__(self):
        self.num = 20

    def print_info(self):
        print(f"num的数值是：{self.num}")

class AB(A, B):
    def __init__(self):
        self.num = 30

    def print_info(self):
        print(f"num的数值是：{self.num}")

    def print_A(self):
        A.__init__(self)
        A.print_info(self)

    def print_B(self):
        B.__init__(self)
        B.print_info(self)

# 孙子类
class ABC(AB):
    pass

abc = ABC()
abc.print_info()
abc.print_A()
abc.print_B()