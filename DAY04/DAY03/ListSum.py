# 4常用的操作方法
'''
    4.1查找
        4.1.1 find()：检测某个子串是否包含在这个字符串中，如果在则返回这个子串开始位置的下标，否则返回-1。
            语法：
                字符串序列，find(子串，开始位置的下标，结束位置的下标)
'''
str = "I love yanandaxue"
print(str.find("yanan", 1, 15))  # 7
print(str.find("yanan"))  # 在整个字符串中找
print(str.find("hello"))

'''
    4.1.2 index()：检测某个子串是否包含在这个字符串中，如果在则返回这个子串开始位置下标，否则包异常。
        语法：
            字符串序列.index(子串，开始位置下标，结束位置下标)
    注意：
        开始和结束位置下标可以省略，表示在整个字符串序列中查找。
'''
my_str = "hello,python! HELLO every one"
print(my_str.index("python"))
print(my_str.index("every", 5, 28))
# print(my_str.index("yanns"))    # ValueError: substring not found

'''
    4.1.3 
    rfind(): 和find()功能相同，但是查找的方向是从右侧开始
    rindex(): 和index()功能相同，但是查找方向从右侧开始
    count(): 返回某个子串在字符串中出现的次数。
'''
mystr = "hello! hello! hello!"
print(mystr.count("hello", 0, 10))
print(mystr.count("hello"))
print(mystr.count("on"))  # 没统计到直接是0

'''
    4.2 修改
        所谓修改字符串，指的就是通过函数的形式修改字符串中的数据。
'''
'''
    4.2.1 replace() 替换
    语法：
        字符串序列.replace(旧子串，新子串，替换次数)
    注意:
        替换次数如果查出子串出现的次数，则替换次数为子串出现的次数
        数据是按照能否直接修改分为可变类型和不可变类型两种，字符串类型的数据修改的时候不能改变原有的字符串，属于不能直接修改数据的类型即是不可变类型。
'''
mystr1 = "hello world and hello yadx and hello python and hello every one"
print(mystr1.replace("and", "he", 10))  # 没有十次的话就有多少次替换多少次
print(mystr1.replace("and", "he", 2))
print(mystr1.replace("and", "he"))

'''
    4.2.2 split() 按照指定字符串进行分隔
    语法：
        字符串序列.split(分隔字符，num)
    注意：
        num表示分割出现的次数，即将来返回数据个数为num +1个
        如果分割字符串是原有字符串的子串，分割后则丢失该子串
'''
mystr1 = "hello world and hello yadx and hello python and hello every one"
print(mystr1.split("and"))
print(mystr1.split("and", 2))
print(mystr1.split(" "))
print(mystr1.split(" ", 2))

'''
    4.2.3 join(): 用一个字符串或子串合并字符串，即是将多个字符串合并为一个新的字符串
        语法：
            字符串子串.join(多字符串组成的序列)
'''
list = ['y', 'a', 'd', 'x']
print('_'.join(list))
print(''.join(list))

list1 = ['I', 'love', 'yadx']
print(' '.join(list1))

'''
    4.2.4 capitalize(): 将字符串的第一个字符转换为大写
    该函数只转换第一个字符 其余还是小写

'''
mystr = "yadx"
print(mystr.capitalize())

'''
    4.2.5 title(): 将字符串每个单词的首字母转化为大写
'''
mystr = "hello yadx hello python"
print(mystr.title())

'''
    4.2.6 lower():将字符串中的大写转小写
'''
mystr = "HELLO PYTHON"
print(mystr.lower())

'''
    4.2.7 upper()：将字符串中的小写转化为大写
'''
mystr = "hello python"
print(mystr.upper())

'''
    4.2.8 
    lstrip():删除字符串左侧空白字符。
    rstrip():删除字符串右侧空白字符。
    strip():删除字符串中的空白字符。
'''

mystr = "   hello Python     "
print(mystr.lstrip())
print(mystr.rstrip())
print(mystr.strip())

#
'''
ljust():返回一个原字符串左对齐，并使用指定字符(默认空格)填充至对应长度的新字符串
    语法：
        字符串序列.ljust(长度，填充字符)
rjust():返回一个原字符串右对齐，并使用指定字符(默认空格)填充至对应长度的新字符串
center():返回一个原字符串居中对齐，并使用指定字符(默认空格)填充至对应长度的新字符串
'''
mystr = "hello"
print(mystr.ljust(10, "p"))
print(mystr.rjust(10, "p"))
print(mystr.center(10, "p"))

'''
    判断：
    所谓判断即是判断真假，返回的结果是布尔类型的数据：True或者是False
    1.stratswith():检查字符串是否以指定子串开头，是返回True，否则返回False，如果设置开始和结束位置的下标，则在指定范围内检查
    语法：
        字符串序列.startSwitch(子串，开始位置的下标，结束位置的下标)
'''
mystr1 = "hello world and hello yadx and hello python and hello everyone"
print(mystr1.startswith("hello"))
print(mystr1.startswith("hello", 5, 20))
'''
    判断：
    所谓判断即是判断真假，返回的结果是布尔类型的数据：True或者是False
    2.endswith():检查字符串是否以指定子串开头，是返回True，否则返回False，如果设置开始和结束位置的下标，则在指定范围内检查
    语法：
        字符串序列.endSwitch(子串，开始位置的下标，结束位置的下标)
'''
print(mystr1.endswith("everyone"))
print(mystr1.endswith("everyone "))
print(mystr1.endswith("everyone", 2, 20))

'''
    3.isalpha()：如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False。
'''
mystr = "hello"
my_str = "hello 1232"
print(mystr.isalpha())
print(my_str.isalpha())

'''
    4.isdigit()：如果字符串只包含数字则返回 True 否则返回 False。
'''
mystr = "hello"
my_str = "hello 1232"
print(mystr.isdigit())
print(my_str.isdigit())

'''
    5.isdigit()：如果字符串至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回
'''
mystr = "hello"
my_str = "hello 1232"
print(mystr.isalnum())
print(my_str.isalnum())


'''
    6.isspace()：如果字符串中只包含空白，则返回True，否则返回False
'''
mystr = "     "
my_str = "hello 1232"
print(mystr.isspace())
print(my_str.isspace())


# 4常用的操作方法
'''
    4.1查找
        4.1.1 find()：检测某个子串是否包含在这个字符串中，如果在则返回这个子串开始位置的下标，否则返回-1。
            语法：
                字符串序列，find(子串，开始位置的下标，结束位置的下标)
'''
str = "I love yanandaxue"
print(str.find("yanan", 1, 15))  # 7
print(str.find("yanan"))  # 在整个字符串中找
print(str.find("hello"))

'''
    4.1.2 index()：检测某个子串是否包含在这个字符串中，如果在则返回这个子串开始位置下标，否则包异常。
        语法：
            字符串序列.index(子串，开始位置下标，结束位置下标)
    注意：
        开始和结束位置下标可以省略，表示在整个字符串序列中查找。
'''
my_str = "hello,python! HELLO every one"
print(my_str.index("python"))
print(my_str.index("every", 5, 28))
# print(my_str.index("yanns"))    # ValueError: substring not found

'''
    4.1.3 
    rfind(): 和find()功能相同，但是查找的方向是从右侧开始
    rindex(): 和index()功能相同，但是查找方向从右侧开始
    count(): 返回某个子串在字符串中出现的次数。
'''
mystr = "hello! hello! hello!"
print(mystr.count("hello", 0, 10))
print(mystr.count("hello"))
print(mystr.count("on"))  # 没统计到直接是0

'''
    4.2 修改
        所谓修改字符串，指的就是通过函数的形式修改字符串中的数据。
'''
'''
    4.2.1 replace() 替换
    语法：
        字符串序列.replace(旧子串，新子串，替换次数)
    注意:
        替换次数如果查出子串出现的次数，则替换次数为子串出现的次数
        数据是按照能否直接修改分为可变类型和不可变类型两种，字符串类型的数据修改的时候不能改变原有的字符串，属于不能直接修改数据的类型即是不可变类型。
'''
mystr1 = "hello world and hello yadx and hello python and hello every one"
print(mystr1.replace("and", "he", 10))  # 没有十次的话就有多少次替换多少次
print(mystr1.replace("and", "he", 2))
print(mystr1.replace("and", "he"))

'''
    4.2.2 split() 按照指定字符串进行分隔
    语法：
        字符串序列.split(分隔字符，num)
    注意：
        num表示分割出现的次数，即将来返回数据个数为num +1个
        如果分割字符串是原有字符串的子串，分割后则丢失该子串
'''
mystr1 = "hello world and hello yadx and hello python and hello every one"
print(mystr1.split("and"))
print(mystr1.split("and", 2))
print(mystr1.split(" "))
print(mystr1.split(" ", 2))

'''
    4.2.3 join(): 用一个字符串或子串合并字符串，即是将多个字符串合并为一个新的字符串
        语法：
            字符串子串.join(多字符串组成的序列)
'''
list = ['y', 'a', 'd', 'x']
print('_'.join(list))
print(''.join(list))

list1 = ['I', 'love', 'yadx']
print(' '.join(list1))

'''
    4.2.4 capitalize(): 将字符串的第一个字符转换为大写
    该函数只转换第一个字符 其余还是小写

'''
mystr = "yadx"
print(mystr.capitalize())

'''
    4.2.5 title(): 将字符串每个单词的首字母转化为大写
'''
mystr = "hello yadx hello python"
print(mystr.title())

'''
    4.2.6 lower():将字符串中的大写转小写
'''
mystr = "HELLO PYTHON"
print(mystr.lower())

'''
    4.2.7 upper()：将字符串中的小写转化为大写
'''
mystr = "hello python"
print(mystr.upper())

'''
    4.2.8 
    lstrip():删除字符串左侧空白字符。
    rstrip():删除字符串右侧空白字符。
    strip():删除字符串中的空白字符。
'''

mystr = "   hello Python     "
print(mystr.lstrip())
print(mystr.rstrip())
print(mystr.strip())


'''
列表的格式：
    [数据1，数据2，数据3，数据4，数据5....]
列表可以一次性存储多个数据，且可以为不同数据类型
列表的作用是一次用存储多个数据，程序员可以对这些数据进行操作有：增、删、改、查
'''
'''
    1.查找
    下标

'''
# name_list = ['张三', '王五', '李四', '赵六', '朱八', '牛牛', '孙悟空']
# print(name_list[2])
# print(name_list[3])

'''
    2.函数
        index():返回指定数据所在位置的下标
        语法：
            列表序列.index(数据，开始位置下标，结束位置下标)
'''
# print(name_list.index("王五", 0, 4))
# 如果查找的数据不存在则就会报错
# print(name_list.index("张以"))    # ValueError: '张以' is not in list

'''
    3.count():统计指定数据在当前列表中出现的次数
'''
# name_list = ['张三', '王五', '张三', '牛牛', '朱八', '张三', '孙悟空']
# print(name_list.count("张三"))

'''
    4.len():访问列表的长度，即列表中的数据的个数
'''
# print(len(name_list))

'''
    5.in: 判断指定数据在某个列表中是否出现，如果在则返回True，否则就返回False
'''
# print("牛牛" in name_list)    # True
# print("张毅" in name_list)    # False

'''
    6.in: 判断指定数据不在某个列表中，如果不在则返回True，否则就返回False
'''
# print("牛牛" not in name_list)    # False
# print("张毅" not in name_list)    # True

'''
    需求：
        查找用户输入的名字是否已经存在
'''

# name = input("请输入一个名字：")
# if name in name_list:
#     print(f"您输入的名字是：{name}，该名字已经存在")
# else:
#     print(f"您输入的名字是：{name}，该名字不存在")


'''
    增加：
        增加指定数据到列表中
        appenda() 列表末尾追加数据
        语法：
            列表序列.append(数据)
    注意：
        列表在追加数据的时候是在原来的列表中追加的数据，故列表是可变类型。
'''
names = ['刘备', '关羽', '张飞']
names.append("赵云")
print(names)
# 如果追加的数据是一个序列，则追加整个序列到列表。
names.append(["孙尚香", "刘禅"])
print(names)

'''
    extend(数据)
        列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一追加到列表中。
'''
names = ['刘备', '关羽', '张飞']
names.extend(['赵云', '曹操', '诸葛亮'])
print(names)

'''
    insert(): 指定位置新增数据
    语法：
        列表序列.insert(位置下标，数据)
'''
names.insert(1, '曹操')
print(names)

'''
    列表的删除
        del
        语法：
        del 目标列表

'''
# name_list = ['张三', '王五', '张三', '牛牛', '朱八', '张三', '孙悟空']
# del name_list
# print(name_list)    # NameError: name 'name_list' is not defined  删除了整个列表

'''
    删除指定数据
    del 目标列表[要删除数据的下标]
'''
# name_list = ['张三', '王五', '张三', '牛牛', '朱八', '张三', '孙悟空']
# del name_list[2]
# print(name_list)

'''
    pop(): 删除指定下标的数据，默认为最后一个，并返回删除的数据
'''
# name_list = ['张三', '王五', '张三', '牛牛', '朱八', '张三', '孙悟空']
# del_name = name_list.pop(2)
# print(del_name)
# print(name_list.pop())  # 没有指定下标默认删除的是最后一个

'''
    remove(): 移除列表中每个数据的第一个匹配项
    语法：
        列表序列.remove(数据)
'''
# name_list = ['张三', '王五', '张三', '牛牛', '朱八', '张三', '孙悟空']
# name_list.remove("孙悟空")
# print(name_list)

'''
    clear(): 清空列表数据，但列表依然存在
'''
name_list = ['张三', '王五', '张三', '牛牛', '朱八', '张三', '孙悟空']
name_list.clear()
print(name_list)

'''
    修改：修改指定下标的数据
'''
# name_list = ['张三', '王五', '张三', '牛牛', '朱八', '张三', '孙悟空']
# name_list[4] = "朱六"
# print(name_list)

'''
    逆置：前后顺序颠倒
    reverse()
'''
# name_list.reverse()
# print(name_list)

'''
    列表的排序：
    sort()
    语法：
        列表序列.sort(key = None, reverse = False)
    注意：
    reverse = False 是升序
    reverse = True 是降序
'''
# num_list = [1, 2, 5, 3, 7, 9, 10, 4, 8]
# num_list.sort(key=None, reverse=False)
# print(num_list)
#
# num_list = [1, 2, 5, 3, 7, 9, 10, 4, 8]
# num_list.sort(key=None, reverse=True)
# print(num_list)

'''
    复制：函数copy()
'''
num_list = [1, 2, 5, 3, 7, 9, 10, 4, 8]
num2_list = num_list.copy()
print(num2_list)

'''
    列表的循环遍历
        for
        while
'''
# while
# name_list = ['张三', '王五', '张三', '牛牛', '朱八', '张三', '孙悟空']
# i = 0
# while i < len(name_list):
#     print(name_list[i], end=" ")
#     i += 1
# print()

# for
# for i in name_list:
#     print(i, end=" ")
# print()

'''
    列表的嵌套
        所谓列表的嵌套指的就是一个列表里包含了其他子列表
'''

# names = [['小红', '小黑', '小花'], ['刘备', '张飞', '关羽'], ['孙悟空', '猪悟能', '沙悟净']]
# print(names[1])
# print(names[1][0])
# 嵌套列表遍历
# for i in names:
#     for j in i:
#         print(j)



