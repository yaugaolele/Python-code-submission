# 3.判定一个年份是闰年还是平年
# 能被4整除而不能被100整除。
# 能被400整除
year = int(input("请输入要判定的年份："))
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print("是闰年")
else:
    print("不是闰年")