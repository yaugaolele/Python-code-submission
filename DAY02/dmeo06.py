# 1.从控制台输入一个三位数，如果是水仙花数就打印“水仙花数”，否则就打印“不是水仙花数”
# 该数的每一位的立方和等于自身的值，比如：153 = 1^3 + 5^3 + 3^3
n = int(input("请输入一个数字："))
a = (n % 10) ** 3   # 拿到个位的三次幂
b = ((n // 10) % 10) ** 3   # 拿到十位的三次幂
c = ((n // 100) % 10) ** 3  # 拿到百位的三次幂
sum = a + b + c
if (sum == n):
    print(f"{n}是水仙花数")
else:
    print(f"{n}不是水仙花数")

# 2.成绩判定，给一个成绩
#    大于85                 打印：优秀
#    大于75 小于等于 85      打印：良好
#    大于等于60 小于75       打印：及格
#    小于60                 打印：不及格

score = int(input("请输入成绩："))
if score > 85:
    print("优秀")
elif 75 < score <= 85:
    print("良好")
elif 60 <= score <= 75:
    print("及格")
else:
    print("不及格")

# 3.判定一个年份是闰年还是平年
# 能被4整除而不能被100整除。
# 能被400整除
year = int(input("请输入要判定的年份："))
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print("是闰年")
else:
    print("不是闰年")

# 4.写出判断一个数是否能同时被3和7整除的条件语句，并且打印对应的结果
count = int(input("请输入一个整数："))
n = count % 3 == 0 and count % 7 == 0
if n == True:
    print(f"{count}可以同时被3和7整除")
else:
    print(f"{count}不可以同时被3和7整除")

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

# 6.编写一个程序，获取一个用户输入的整数，然后通过程序显示这个数是奇数还是偶数
n = int(input("请输入一个数字："))
if n % 2 == 0:
    print(f"{n}是偶数")
if n % 2 == 1:
    print(f"{n}是奇数")