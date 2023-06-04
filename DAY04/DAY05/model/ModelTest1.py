'''
    Python中模块(model)是一个Python的文件，以.py结尾，包含了Python对象定义和Python语句
    模块能定义函数、类、变量、模块里也能包含可执行的代码
    导入模块的方式：
        1.import 模块名
        2.from 模块名 import 功能名
        3.from 模块名 import *
        4.import 模块名 as 别名
        5.from 模块名 import 功能名 as 别名
'''
'''
导入方式：
    语法：
        import 模块名
        import 模块名1， 模块名2....
        
调用功能：
    模块名.功能名
'''
import math
print(math.sqrt(9)) # 3.0

'''
导入方式：
    语法：
        from 模块名 import 功能名1, 功能名2...
'''
from math import sqrt
print(sqrt(9))  # 3.0

'''
导入方式：
    语法：
        from 模块名 import *
'''
from math import *
print(ceil(3.9))    # 4
print(floor(3.9))    # 3

'''
模块定义起别名：
    import 模块名 as 别名
    
功能定义起别名：
    from 模块名 import 功能名 as 别名
'''
import time as tt
tt.sleep(2)
print("hello")

from time import sleep as s
s(3)
print("world")

