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
