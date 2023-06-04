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

