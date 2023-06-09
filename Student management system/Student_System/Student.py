# 实现一个命令行版本的学生管理系统
import os.path
import sys

# 使用这个全局变量，来管理所有的学生信息
# 这个列表的每个元素都是一个“字典”，每个字典就分别表示了一个同学
students = []

def save():
    """
    用于存档
    """
    # 此处的路径不是以 d: 开头的绝对路径，是相对路径，
    # 此时这个写法的含义就是让record.txt和当前的student.py在同一个目录中

    with open('record.txt', 'w', encoding='utf8') as f:
        for s in students:
            f.write(f"{s['studentId']}\t{s['name']}\t{s['gender']}\t{s['className']}\n")
        print(f'[存档成功] 共存储了{len(students)}条记录！')
def load():
    """
    用于读档
    """
    # 如果读档文件不存在，则直接跳过读档
    # 为了避免读方式打开文件的时候，文件不存在引起异常
    if not os.path.exists('record.txt'):
        return
    # 读档的时候保证先把旧的数据给清理干净
    global students
    students = []
    with open('record.txt', 'r', encoding='utf8') as f:
        for line in f:
            # 针对这一行数据，按照\t进行切分操作
            # 切分之前，要除去末尾的换行
            line = line.strip()
            tokens = line.split('\t')
            if len(tokens) != 4:
                print(f"当前行格式存在问题！ line = {line}")
                continue
            student = {
                'studentId': tokens[0],
                'name': tokens[1],
                'gender': tokens[2],
                'className': tokens[3]
            }
            students.append(student)
        print(f"[读档成功]共读取了{len(students)}条记录！")
def menu():
    print(' 1.新增学生')
    print(' 2.显示学生')
    print(' 3.查找学生')
    print(' 4.删除学生')
    print(' 5.修改信息')
    print(' 0.退出程序')
    choice = input("请输入您的选择：")
    return choice

def insert():
    print('[新增学生] 开始！')
    studentId = input("请输入学生的学号：")
    name = input("请输入学生的姓名：")
    gender = input("请输入学生的性别：")
    if gender not in ('男', '女'):
        print("输入的内容不符合要求，新增失败！")
        return
    className = input("请输入学生的班级：")
    # 使用一个字典把上述的信息给集合起来
    student = {
        'studentId': studentId,
        'name': name,
        'gender': gender,
        'className': className
    }
    global students
    students.append(student)
    # 增加一个保存操作
    save()
    print('[新增学生] 完毕！')


def show():
    # 遍历全局变量的这个列表，把每个学生的信息给打印出来
    print('[显示学生] 完毕！')
    for s in students:
        print(f"[{s['studentId']}]\t{s['name']}\t{s['gender']}\t{s['className']}")
    print(f'[显示学生]完毕！ 共显示了{len(students)}条数据！')



def find():
    # 根据学生姓名，进行查找
    print("[查找学生] 开始！")
    name = input("请输入要查找的同学姓名：")
    count = 0
    for s in students:
        if name == s['name']:
            print(f"[{s['studentId']}]\t{s['name']}\t{s['gender']}\t{s['className']}")
            count += 1
    print(f"[查找学生] 结束！共找到了{count}个匹配的学生！")

def delete():
    print("[删除学生] 开始！")
    studentId = input("请输入要删除的学生的学号：")
    # 看看这个学号对应的同学是哪个字典，然后把这个字典从列表中删除掉就可以了。
    for s in students:
        if studentId == s['studentId']:
            print(f"删除{s['name']}同学的信息！")
            students.remove(s)
    save()
    print("[删除学生] 结束！")


def update():
    print("[修改信息] 开始！")
    while True:
        studentId = input("请输入要修改的学生的学号：")
        # 检查学生是否存在
        for s in students:
            if studentId == s['studentId']:
                # 如果存在显示该学生的信息
                print(f"{s['studentId']}\t{s['name']}\t{s['gender']}\t{s['className']}")
                update_flag = input("确定是否修改：(yes or no)")
                if update_flag == 'yes':
                    s['studentId'] = input("请输入学号：")
                    s['name'] = input("请输入姓名：")
                    s['gender'] = input("请输入性别：")
                    s['className'] = input("请输入班级：")
                    save()
                    # 修改了目标学员后退出循环
                    return

        print("输入学员学号有误，请重新输入")
    # 增加修改后的数据
    print("[修改信息] 结束！")


def main():
    """入口函数"""
    # 通过控制台和用户进行交互
    print("---------------------------------------")
    print("           欢迎来到学生管理系统          ")
    print("---------------------------------------")
    # 在程序启动的时候调用一次load()！
    load()
    while True:
        # 通过 menu 函数来打印出菜单项
        choice = menu()
        if choice == '1':
            # 新增学生
            insert()
        elif choice == '2':
            # 显示所有学生
            show()
        elif choice == '3':
            # 查找学生
            find()
        elif choice == '4':
            # 删除学生
            delete()
        elif choice == '5':
            # 修改信息
            update()
        elif choice == '0':
            # 退出系统
            print("goodbye!")
            sys.exit(0)
        else:
            print("您的输入有误，请重新输入！")
            # 需要进行下次循环，让用户重新输入
            # continue


main()