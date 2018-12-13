class Gun(object):
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, num):
        self.bullet_count += num

    def shoot(self):
        if self.bullet_count <= 0:
            print("[%s]还没有子弹，请先装填子弹" % self.model)
        else:
            self.bullet_count -= 1
            print("突突突突。。。。。子弹还剩[%d]" % self.bullet_count)


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:
            print("士兵[%s]还没有枪，请先领枪" % self.name)
            return
        else:
            self.gun.add_bullet(100)
            self.gun.shoot()


gun = Gun("ak47")
soldier = Soldier("冷锋")
soldier.gun = gun
soldier.fire()


class Bird:

    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("开始吃东西了")
            self.hungry = False
        else:
            print("吃饱了，不想吃了")


class SongBird(Bird):

    def __init__(self):
        super().__init__()
        self.sound = "jiu jiu jiu"

    def sing(self):
        print(self.sound)


bird = SongBird()
bird.eat()
bird.eat()
bird.sing()


class Rectangle:

    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height

    # 获取方法在前，设置方法在后
    size = property(get_size, set_size)
    #  不指定参数，不能读也不能写
    not_read_and_write = property()
    # 指定一个参数,只能读，不能写
    could_read_not_write = property(get_size)


rectangle = Rectangle()
rectangle.height = 100
rectangle.width = 10
print(rectangle.size)
rectangle.size = 300, 200
print(rectangle.width)
# print(rectangle.not_read_and_write)
print(rectangle.could_read_not_write)
# rectangle.could_read_not_write = 60, 30


i = iter([1, 2, 3])
for j in i:
    try:
        print(j)
    except :
        raise Exception("wrong")
