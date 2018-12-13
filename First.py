import random

print("Hello python")
print("hello python\n" * 8)
print("你好" * 8)
print(5 / 2)
"""
这里面是注释，可以随便打哦
"""
a = 23
b = 15
if a >= 10 and b >= 10:
    print("hello")
else:
    print("go away")

is_employee = True
if is_employee is True:
    print("好好工作")
else:
    print("非本公司请勿入内")

holiday_name = input("请输入节日名称")

if holiday_name == "情人节":
    print("出去开房啊")
elif holiday_name == "新年":
    print("各回各家")
elif holiday_name == "元旦":
    print("家里躺尸")
else:
    print("有没有女朋友心理没有ABCD数吗？")

randint = random.randint(0, 10)
print(randint)

i = 0
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1


def say_hello(name):
    """定义函数，函数的文档注释"""
    print(name)


say_hello("张三")
