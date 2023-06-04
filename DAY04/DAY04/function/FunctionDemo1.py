'''
    函数就是将一段具有独立功能的代码块，整合到一个整体并命名，在需要的位置调用这个名称即可完成对应的需求。
    1.定义函数
        def 函数名(参数)：
            代码1
            代码2
            ...
    2.调用函数
    函数名(参数)
注意：
    1.在不同的需求，参数可有可无
    2.在Python中，函数必须先定义，后使用
'''
# 需求：ATM机取款
# 搭函数框架
# 注意：一定是先定义函数在使用函数
def select_fun():
    print("------请选择功能-------")
    print("查询余额")
    print("存款")
    print("取款")


print("密码正确，登录成功")
select_fun()
# 显示"选择功能"界面
print("查询余额完成")
select_fun()
# 显示"选择功能"界面
print("取了2000元钱")
select_fun()
# 显示"选择功能"界面

# 封装"选择功能"
