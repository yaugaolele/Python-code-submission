# 字典的循环遍历
dict1 = {"name": "张三", "age": 20, "sex": "男"}
# 循环遍历所有的键key
for key in dict1.keys():
    print(key)
print("=====================")

# 遍历所有的值
for value in dict1.values():
    print(value)
print("===================")

# 遍历字典中的元素
for item in dict1.items():
    print(item)
print("===================")

# 遍历所有的键值对
for key, value in dict1.items():
    print(f"{key}: {value}")

