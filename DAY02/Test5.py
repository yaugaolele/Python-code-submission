# 5.写出判断一个数是否能被3或7整除，但是不能同时被3或7整除，并且打印对应的结果
count = int(input("请输入一个数："))
if (count % 3 == 0 or count % 7 == 0):
    if (count % 3 != 0 and count % 7 == 0):
        print(f"{count}可以被7整除，但是不可以被3整除，满足条件")
    elif (count % 3 == 0 and count % 7 != 0):
        print(f"{count}可以被3整除，但是不可以被7整除，满足条件")
    else:
        print(f"{count}既可以被3整除也可以被7整除，不满足条件")
else:
    print(f"{count}即不可以被3整除也不可以被7整除，不满足条件")



