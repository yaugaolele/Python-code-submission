# 4.写出判断一个数是否能同时被3和7整除的条件语句，并且打印对应的结果
count = int(input("请输入一个整数："))
n = count % 3 == 0 and count % 7 == 0
if n == True:
    print(f"{count}可以同时被3和7整除")
else:
    print(f"{count}不可以同时被3和7整除")

