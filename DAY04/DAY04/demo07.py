# 循环可以配合else使用，else下缩进的代码指定是当循环正常结束之后要执行的代码
'''
    语法：
        while 条件：
            重复执行代码1
        else：
            循环正常结束之后要执行的代码
'''
# i = 1
# while i <= 5:
#     print("努力学习！")
#     i += 1
# else:
#     print("最终拿到offer！")
# print("====================")
# 退出循环的方式
# break
# i = 1
# while i <= 5:
#     if i == 3:
#         print("没有好好上课！,回家卖红薯")
#         break
#     print("努力学习！")
#     i += 1
# else:
#     print("最终拿到offer！")

'''
    所谓else指的是循环正常结束之后要执行的代码，如果循环非正常结束（break）else下的代码就不执行了
'''
# print("====================")

# 退出循环的方式
# break
# i = 1
# while i <= 5:
#     if i == 3:
#         print("没有好好上课！")
#         i += 1
#         continue
#     print("努力学习！")
#     i += 1
# else:
#     print("最终拿到offer！")
'''
    因为continue是退出当前循环，继续执行下一次循环，所以该循环在continue控制下可以正常结束
'''

'''
     for 循环配合else
     语法：
        for临时变量 in 序列：
            重复执行的代码
        else:
            循环正常结束执行的代码
'''
# str = 'yandaxue'
# for i in str:
#     print(i)
# else:
#     print("循环正常结束")

# 退出方式
'''
    break:
'''
# str = "yanandaxue"
# for i in str:
#     if i == "u":
#         print("遇到U不打印")
#         break
#     print(i)
# else:
#     print("循环正常结束")

'''
    continue:
'''
str = "yanandaxue"
for i in str:
    if i == "u":
        print("遇到U不打印")
        continue
    print(i)
else:
    print("循环正常结束")