from string import Template
from math import sqrt

nameList = ["张三", "李四", "王五"]
print(nameList.index("王五"))
print(len(nameList))

for name in nameList:
    index = nameList.index(name)
    print("我的角标是%s" % index)
    print(name)

user = {"name": "张三",
        "age": 24,
        "address": "浙江杭州"}

user["gender"] = -1
print(user)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[7:])

database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '9527'],
    ['jones', '6666']
]
# username = input("请输入用户姓名")
# pin = input("请输入code")
# if [username, pin] in database:
#   print("%s登陆成功" % username)
x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len, reverse=True)
print(x)
print(list('python'))
temp1 = Template("Hello,$who! $what enough for ya?")
print(temp1.substitute(who="Mars", what="Dusty"))
print("{}, {} and {}".format("first", "second", "third"))
# 按索引进行操作
print("{0}, {1} and {2}".format("first", "second", "third"))
print("{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to"))

x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
# 替换掉副本中的值，原件不会受到影响
y['username'] = 'mlh'
# 修改副本中的值，原件也将发生变化，因为原件指向的也是被修改的值
y['machines'].remove('bar')
print(y)
print(x)

name = "xiaoming"
status = "firend" if name.endswith("ming") else "stranger"
print(status)

for number in range(0, 10):
    print(number)
seasons = ['spring', 'summer', 'fall', 'winter']
# 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
print(list(enumerate(seasons)))
for i, season in enumerate(seasons):
    print(i, season)

for n in range(99, 0, -1):
    root = sqrt(n)
    n = int(root)
    print(root, n)

range_ = [x * x for x in range(10)]
print(range_)


def print_params(*params):
    print(params)


print_params("hello", "meimei")
print_params()


def in_the_middle(x, *y, z):
    print_params(x, y, z)


in_the_middle(1, 2, 3, 4, 5, z=66)

x = 3


def print_params3(**params):
    global x
    x = x + 1
    print(x)
    print(params)


print_params3(x=1, y=2, z=3, f=4)


def multiplier(factor):
    def multiplier_by_factor(number):
        return number * factor

    return multiplier_by_factor


# 作用域嵌套，闭包
double = multiplier(2)
result = double(3)
print(result)


def facorial(n):
    if n == 1:
        return 1
    else:
        return n * facorial(n - 1)


print(facorial(4))

# 异常捕获
try:
    x = int(input("请输入第一个数"))
    y = int(input("请输入第二个数"))
    print(x/y)
except ZeroDivisionError:
    print("被除数不能为0")
finally:
    print("it's done")
