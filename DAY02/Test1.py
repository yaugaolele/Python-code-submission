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

