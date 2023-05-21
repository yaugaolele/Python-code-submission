'''
    循环控制语句：
        break：中断循环
        continue：结束当前一次循环继续执行下一次循环
'''
i = 1
while i <= 5:
    if i == 3:
        print("吃饱了不想吃了")
        break # 中断循环
    print(f"吃了{i}个苹果")
    i += 1
print("循环结束")

print("===================")

j = 1
while j <= 5:
    if j == 3:
        print(f"有虫子，不想吃第{j}个苹果了")
        j += 1
        # 在continue之前一定要修改计数器，否则就会陷入死循环
        continue
    print(f"吃了第{j}个苹果")
    j += 1
print("循环结束")
