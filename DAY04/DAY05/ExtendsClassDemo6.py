'''
    super() :调用父类方法
'''
class Master(object):
    def __init__(self):
        self.peifang = "[古法煎饼果子配方]"

    def make_cake(self):
        print(f"运用{self.peifang}制作煎饼果子")

class A(Master):
    def __init__(self):
        self.peifang = "[新式煎饼果子配方]"

    def make_cake(self):
        print(f"运用{self.peifang}制作煎饼果子")
        # 方法1
        # super(A, self).__init__()
        # super(A, self).make_cake()
        # 方法2
        super().__init__()
        super().make_cake()

class B(A):
    def __init__(self):
        self.peifang = "[独创煎饼果子配方]"

    def make_cake(self):
        print(f"运用{self.peifang}制作煎饼果子")

    # 子类调用父类同名的方法和属性，把父类的同名属性和方法再次封装
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_A_cake(self):
        A.__init__(self)
        A.make_cake(self)

    def make_old_cake(self):
        # 代码冗余 父类类名如果变化，这里代码需要平凡修改
        # 方法一：
        Master.__init__(self)
        Master.make_cake(self)
        A.__init__(self)
        A.make_cake(self)

        # 方法二：
        # super(当前类名, self).函数
        super(B, self).__init__()
        super(B, self).make_cake()

        # 方法三：
        # super().函数
        super().__init__()
        super().make_cake()

# 注意：使用super可以自动查找父类，调用顺序遵循__mor__类属性的顺序，比较适合单继承。
a = A()
a.make_cake()
b = B()
b.make_cake()
b.make_old_cake()