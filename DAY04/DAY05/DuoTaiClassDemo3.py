'''
    类方法和静态方法
'''
'''
类方法：
    特点：
        第一个形参是类对象的方法
        需要用装饰器@classmethod来标识为其类方法，对类方法，第一个参数必须是类对象，一般cls作为第一个参数
    使用场景：
        当方法需要使用类对象（如访问私有类属性等）时，定义类方法
        类方法一般和类属性配合使用
'''
class Person(object):
    __age = 18
    @classmethod
    def get__age(cls):
        return cls.__age

p = Person()
age = p.get__age()
print(age)

'''
静态方法：
    特点：
        需要通过装饰器@staticmethod进行修饰，静态方法即不需要传递类对象，也不需要传递实例对象（形参没有self/cls）
        静态方法也能过通过实例对象和类对象进行访问
    使用场景：
        当方法中既不需要使用实例对象/实例属性，也不需要类对象（如类属性和类方法、或者是创建实例）时，定义静态方法。
        取消不需要的参数传递，有利于减少不必要的内存占用和性能消耗
'''
class Student(object):
    @staticmethod
    def info_print():
        print("这是一个学生类")

# 静态方法即可以使用对象访问又可以使用类访问
s = Student()
s.info_print()
Student.info_print()