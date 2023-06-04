'''
    添加和获取对象的属性
    属性就是特征，比如洗衣机的宽度、高度、容量....
    对象的属性即可以在类的外面添加和获取，也可以在类的里面添加和获取
'''
'''
    1.类的外面添加对象的属性
    语法：
        对象名.属性名 = 值
    类外面获取对象属性
    语法：
        对象名.属性名
'''
class Person():
    def print_info(self):
        print("输出学生的信息：")

p = Person()
p.name = "张三"
p.age = 18
print(f"学生的姓名为：{p.name}")
print(f"学生的年龄为：{p.age}")
# 学生的姓名为：张三
# 学生的年龄为：18
print("===================")
'''
    在类里面获取对象属性
'''
class Person():
    def print_info(self):
        print("输出学生信息：")
        print(f"输出学生的姓名：{self.name}")
        print(f"输出学生的年龄：{self.age}")

# 创建person对象
p = Person()

p.name = "张三"
p.age = 19

'''
在类内获取对象属性
语法：
    self.属性
'''
p.print_info()