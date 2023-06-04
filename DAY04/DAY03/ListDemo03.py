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



