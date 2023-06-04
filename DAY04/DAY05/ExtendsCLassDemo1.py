'''
    类的继承
    Python面向对象的继承指的是多个类之间的所属关系，即子类默认继承所有属性和方法
    在Python中所有类的父类都是Object
'''
# 父类
class Fu(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)

# 子类
class Zi(Fu):
    pass

zi = Zi()
zi.info_print()     # 1


