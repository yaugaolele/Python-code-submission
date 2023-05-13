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


