'''
五.综合应用5.1烤地瓜
5.1.1需求
需求主线∶
    1．被烤的时间和对应的地瓜状态︰
        0-3分钟∶生的
        3-5分钟︰半生不熟
        5-8分钟︰熟的
        超过8分钟︰烤糊了
    2．添加的调料∶
        用户可以按自己的意愿添加调料

5.1.2步骤分析
    需求涉及一个事物︰地瓜﹐故寨例涉及一个类∶地瓜类.

5.1.2.1定义类
    地瓜的属性
        ●被烤的时间。
        ●地瓜的状态。
        ●添加的调料
    地瓜的方法
        被烤
            ●用户根据意愿设定每次烤地瓜的时间
            ●判断地瓜被烤的总时间是在哪个区间﹐修改地瓜状态
        添加调料
            ●用户根据意愿设定添加的调料
            ●将用户添加的调料存储
        显示对象信息
'''
# 定义类
# 地瓜的属性  地瓜的出书化  后续根据需求更新实例属性

class SweetPotato():
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 地瓜的状态
        self.cook_static = "生的"
        # 调料的列表
        self.coodingments = []

    def cook(self, time):
        """烤地瓜的方法"""
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_static = "生的"
        elif 3 <= self.cook_time <5:
            self.cook_static = "半生不熟"
        elif 5 <= self.cook_time < 8:
            self.cook_static = "熟了"
        elif self.cook_time >= 8:
            self.cook_static = "烤糊了"

    # 添加掉料
    def add_coodingments(self, coodingments):
        self.coodingments.append(coodingments)

    # 输出对象的状态
    def __str__(self):
        return f"这个地瓜烤了{self.cook_time}分钟了，目前的状态是{self.cook_static},添加的调料有：{self.coodingments}"



# 创建对象 测试实例属性和实例方法
dogua1 = SweetPotato()
print(dogua1)   # 这个地瓜烤了0分钟了，目前的状态是生的

dogua1.cook(2)
dogua1.add_coodingments("冰糖")
print(dogua1)   # 这个地瓜烤了2分钟了，目前的状态是生的

dogua1.cook(2)
dogua1.add_coodingments("辣椒面")
print(dogua1)   # 这个地瓜烤了7分钟了，目前的状态是熟了