'''
    多态指的是一类事务有多种形态，（一个抽象类有多个子类，因而多态的概念依赖于继承）
    多态是一种使用对象的方式，子类重写父类方法，调用不同的子类对象的相同父类方法，可以产生不同的执行结果
    多态的优点：
        调用灵活，有了多态可以简化代码，作出通用编程，以适应需求的不断变化
    实现步骤：
        1.定义父类，并提供公共方法
        2.定义子类，并重写父类方法
        3.传递子类对象给调用者，可以看到不同子类执行的效果不同
'''
class Animal(object):
    def eat(self): # 提供了统一的方法，哪怕是空方法也可以用
        print("动物吃东西")

class Dog(Animal):  # 继承了Animal
    def eat(self): # 重写了父类的方法
        print("狗吃狗粮")

class Cat(Animal):  # 继承了Animal
    def eat(self): # 重写了父类的方法
        print("猫吃猫粮")

class Person(object):
    def feedAnimal(self, animal):
        animal.eat()

dog = Dog()
cat = Cat()
man = Person()

# 多态的体现
man.feedAnimal(dog)     # 狗吃狗粮
man.feedAnimal(cat)     # 猫吃猫粮
