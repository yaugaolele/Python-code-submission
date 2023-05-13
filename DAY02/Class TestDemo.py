'''
    猜拳游戏
        需求：
            人机大战
            玩家：
                手动出拳
            电脑:
                随机出拳
            判断输赢：
                玩家获胜
                    玩家    电脑
                    石头    剪刀
                    布      石头
                平局
                    玩家出拳 和 电脑出拳相同
                电脑胜利
                    随机出拳，如果玩家不获胜，电脑获胜
        提示：0 - 石头    1 - 剪刀   2 - 布
'''


# 1.导入random的模块
# import 模块名导入模块
# 2.使用random模块中随机整数功能
# random.randint(开始，结束)


# 导入random模块
import random
# 2.计算电脑出拳的随机数字
computer = random.randint(0, 2)
print(computer)

# 玩家
player = int(input("请出拳： 0 - 石头  1 - 剪刀   2 - 布："))

# 玩家获胜 p0:c1  p1:c2   p2:c0
# 判断
if (player == 0) and (computer == 1) or (player == 1) and (computer == 2) or (player == 2) and (computer == 0):
    print("玩家获胜！")
elif player == computer:
    print("平局！")
elif 2 > player or player < 0:
    print("玩家出拳不符合规则！请重新开始！")
else:
    print("电脑获胜！")





