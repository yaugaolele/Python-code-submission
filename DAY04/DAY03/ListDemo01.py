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
    
'''





