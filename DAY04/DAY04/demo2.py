# 利用while循环统计1 - 100 之间的累加和
i = 1
sum = 0
while i <= 100:
    sum += i    # 累加和
    i += 1  # 循环变量的改变
print(sum)

# 练习： 利用while循环计算1 - 100 之间的偶数和

# 方法一
j = 1
sum1 = 0
while j <= 100:
    if j % 2 == 0:
        sum1 += j
    j += 1
print(sum1)

# 方法二
i = 2
sum = 0
while i <= 100:
    sum += i
    i += 2
print(sum)

