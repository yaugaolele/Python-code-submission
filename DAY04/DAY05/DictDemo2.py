'''
    字典的常见操作
'''
# 增
# 语法：字典序列的[key] = 值
# 注意： 如果key存在则修改这个key对应的值，如果key不存在则新增此键值对
dict1 = {"name": "张三", "age": 20, "sex": "男"}
dict1["name"] = "Tom"   # {'name': 'Tom', 'age': 20, 'sex': '男'}
print(dict1)
dict1["id"] = 10
print(dict1)    # {'name': 'Tom', 'age': 20, 'sex': '男', 'id': 10}
# 注意：字典为可变类型

# 删 del()或者del 删除字典或删除字典中指定的键值对
dict2 = {"name": "张三", "age": 20, "sex": "男"}
del dict2["sex"]
print(dict2)    # {'name': '张三', 'age': 20}

# 清空字典clear()
dict3 = {"name": "张三", "age": 20, "sex": "男"}
dict3.clear()
print(dict3)    # {}

# 改 语法：字典序列[k] = 值
# 注意： 如果key存在则修改这个key对应的值，如果key不存在则新增此键值对
dict2["age"] = 19
print(dict2)    # {'name': '张三', 'age': 19}

# 查
# 1.按照key值查找
dict5 = {"name": "张三", "age": 20, "sex": "男"}
print(dict5["name"])    # 张三  如果存在返回value值
# print(dict5["id"])  # KeyError: 'id' 如果当前查找的key不存在就报错

# 2.get()
# 语法：
# 字典序列.get(key, 默认值)
# 注意： 如果当前查找的key不存在则返回第二参数(默认值)，如果省略第二个参数，则返回None
dict6 = {"name": "张三", "age": 20, "sex": "男"}
print(dict6.get("name"))    # 张三
print(dict6.get("id", 101))     # 101
print(dict6.get("id"))      # None

# 3.keys() 获取当前字典中所有的key
dict7 = {"name": "张三", "age": 20, "sex": "男"}
print(dict7.keys())     # dict_keys(['name', 'age', 'sex'])

# 4.values() 获取当前字典中所有的values
dict8 = {"name": "张三", "age": 20, "sex": "男"}
print(dict8.values())   # dict_values(['张三', 20, '男'])

# 5.items() 获取字典中的所哟键值对
dict9 = {"name": "张三", "age": 20, "sex": "男"}
print(dict9.items())    # dict_items([('name', '张三'), ('age', 20), ('sex', '男')])