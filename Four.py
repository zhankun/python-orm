import fileinput
# w = open("/Users/zhankun/Desktop/test.txt")


with open("/Users/zhankun/Desktop/test.txt") as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line)


print("-----------我是万恶的分割线------------")
with open("/Users/zhankun/Desktop/test.txt") as file:
    for line in file.readlines():
        print(line)


print("-----------我是万恶的分割线------------")
# 使用fileinput实现延迟迭代，减少内存占用
for line in fileinput.input("/Users/zhankun/Desktop/test.txt"):
    print(line)


print("-----------我是万恶的分割线------------")
with open("/Users/zhankun/Desktop/test.txt") as f:
    for line in f:
        print(line)