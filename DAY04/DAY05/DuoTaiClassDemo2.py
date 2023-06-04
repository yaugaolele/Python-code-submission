'''
    类属性和实例属性
'''
# 设置和访问类属性
# 类属性就是类对象所拥有的属性，它被该类的所有对象共有
# 类属性可以使用类对象或实例对象访问
class Person(object):
    age = 18

p1 = Person()
p2 = Person()
print(Person.age)   # 使用类对象访问
print(p1.age)   # 使用实例对象访问
print(p2.age)   # 使用实例对象访问

'''
    类属性的优点：
        1.类的实例，记录的某项数据始终保持一致时，则可以定义类属性
        2.实例属性，要求每个对象为其单独开辟一份内存空间，来记录数据，而类属性为全类所共有，仅占用一份内存，更加节省内存空间
    修改类属性：
        类属性只能通过类对象修改，不能通过实例对象修改，如果通过实例对象修改类属性，表示的是创建了一个实例属性
'''

# 修改类属性
Person.age = 20
print(Person.age)
print(p1.age)
print(p2.age)

# 不能通过实例化对象来修改属性，如果这样操作实则是创建了一个实例属性
p1.age = 19
print(Person.age)   # 20
print(p1.age)   # 19
print(p2.age)   # 20

'''
    实例属性
'''
class Student(object):
    def __init__(self):
        self.age = 18

    def info_print(self):
        print(self.age)

s = Student()
print(s.age)    # 18
# print(Student.age)  # AttributeError: type object 'Student' has no attribute 'age'
# 实例属性不能通过类访问