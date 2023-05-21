# 4常用的操作方法
'''
    4.1查找
        4.1.1 find()：检测某个子串是否包含在这个字符串中，如果在则返回这个子串开始位置的下标，否则返回-1。
            语法：
                字符串序列，find(子串，开始位置的下标，结束位置的下标)
'''
str = "I love yanandaxue"
print(str.find("yanan", 1, 15)) #7
print(str.find("yanan"))    # 在整个字符串中找
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
print(mystr.count("on"))    # 没统计到直接是0

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
