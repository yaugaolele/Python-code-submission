'''
单继承

'''
# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = "[古法煎饼果子配方]"

    def make_ckae(self):
        print(f"使用{self.kongfu}来制造煎饼果子")

# 徒弟类
class Apprentice(Master):
    pass

# 创建徒弟类对象
apprentice1 = Apprentice()
print(apprentice1.kongfu)
apprentice1.make_ckae()
