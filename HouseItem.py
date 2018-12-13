class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s]占地%.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, total_area):
        self.house_type = house_type
        self.total_area = total_area
        self.free_area = total_area
        self.house_item = []

    def __str__(self):
        return ("户型是：%s\n总面积：%.2f[剩余面积：%.2f]\n家具：%s"
                % (self.house_type, self.total_area, self.free_area, self.house_item))

    def add_item(self, item):
        if item.area > self.free_area:
            print("你的房子太小了，剩余面积不足，心里没点B数吗？")
            return
        else:
            detail = {}
            detail["name"] = item.name
            detail["area"] = item.area
            self.house_item.append(detail)
            self.free_area -= item.area


bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.2)
house = House("三室两厅", 89)
house.add_item(bed)
house.add_item(chest)
house.add_item(table)
print(house)
print(house.house_item)
