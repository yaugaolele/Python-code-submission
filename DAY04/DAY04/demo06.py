# for循环
'''
    语法：
        for 临时变量 in 序列：
            重复执行代码
            ......
'''
#
# 配合 break
# str = "yanandaxue"
# for i in str:
#     if i == 'd':
#         print("遇到d不打印")
#         break
#     print(i)

# 配合continue
str = "yananun"
for i in str:
    if i == 'u':
        print("遇到u不打印")
        continue
    print(i)