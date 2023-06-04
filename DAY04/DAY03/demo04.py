# while循环的嵌套
'''
    while 循环嵌套
    语法：
        while 条件1：
            语句1
            ...
            while 条件2：
                语句2
                ...
总结： 所谓while循环嵌套，就是一个while里面嵌套了一个while循环的写法，每个while循环的语法都是一样的
'''
j = 1
while j <= 3:
    i = 1
    while i <= 3:
        print("学习")
        i += 1
    print(f"学习的第{j}天")
    print(f"第{j}天的学习结束")
    j += 1
print("拿到offer！！！")
