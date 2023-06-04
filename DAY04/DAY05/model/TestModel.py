# 导入自定义模块并起别名，
# import ModelTest2 as test
#
# # 调用自定义模块的功能
# test.testA(1, 2)

from ModelTest2 import my_test as test2
from ModelTest3 import my_test as test3
# 当导入多个模块时，且模块内有同名功能，当调用同名功能时，调用到的是后面导入的模块的功能
# 解决问题的办法就是其别名
test2(3, 2)
test3(2, 3)


