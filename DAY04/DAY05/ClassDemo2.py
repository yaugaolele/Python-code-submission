'''
    self 指的是调用该函数的对象
    发现调用当前函数的对象的内存地址与当前方法中的self的内存地址一致
'''
# 1.定义一个类
class Washer():
    def wash(self):
        print("我会洗衣服")
        print(self) # <__main__.Washer object at 0x0000022B26C69160>

# 2.创建一个对象
haier1 = Washer()   # <__main__.Washer object at 0x0000022B26C69160>
print(haier1)

# haier1调用实例方法
haier1.wash()
# 新创建一个对象后两个内存地址不一样
haier2 = Washer()   # <__main__.Washer object at 0x0000022B26C69640>
print(haier2)
