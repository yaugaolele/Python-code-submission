# 课堂练习：
'''
    用* 打印一个正方形
'''
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print(" * ", end="")
        j += 1
    print()
    i += 1

'''
    用* 打印一个三角形
'''
i = 1
while i <= 3:
    # 打印每一行的空格
    k = 1
    while k <= 3 - i:
        print(" ", end=" ")
        k += 1
    j = 1
    # 打印每一行的*
    while j <= (2 * i - 1):
        print("*", end=" ")
        j += 1
    print()
    i += 1

'''
    用循环完成9 * 9 乘法表
'''
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{i} * {j} = {i * j} ", end=" ")
        j += 1
    print()
    i += 1
