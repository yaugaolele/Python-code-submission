'''
练习：
5.2搬家具
    5.2.1需求
        将小于房子刺余面积的家具摆放到房子中
    5.2.2步骤分析
        需求涉及两个事物﹔房子和家具﹐故被寨例涉及两个类∶房子类和家具类·
        5.2.2.1定义类
            房子类
                实例属性
                    ●房子地理位置
                    ●房子占地面积
                    ●房子剩余面积
                    ●房子内家具列表。
                实例方法
                    ●容纳家具
                显示房屋信息

            家具类
                ●家具名称
                ●家具占地面积

        5.2.2.2创建对象并调用相关方法
'''

# 房子类
class Home():
    def __init__(self, address, area):
        self.home_location = address
        self.home_area = area
        self.home_residual_area = area
        self.home_furniture_list = []

    # 容纳家具
    def accommodate_furniture(self, item):
        if self.home_residual_area >= item.furniture_area:
            self.home_furniture_list.append(item.furniture_name)
            self.home_residual_area -= item.furniture_area
        else:
            print("家具太大，剩余面积不足，无法容纳")


    # 显示房屋信息
    def __str__(self):
        return f"房子坐落于：{self.home_location},占地面积：{self.home_area},目前房子剩余面积为：{self.home_residual_area}, 房屋内的家具有：{self.home_furniture_list}"



# 家具类
class Furniture():
    def __init__(self, name, area):
        self.furniture_name = name
        self.furniture_area = area

jia1 = Home("北京",1800)
bed = Furniture("双人床", 6)
print(jia1)
jia1.accommodate_furniture(bed)
print(jia1)
