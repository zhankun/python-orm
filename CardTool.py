cardList = []


def insert_card():
    print("--------开始新增名片------")
    name = str(input("清输入用户名"))
    phone = str(input("请输入电话号码"))
    email = str(input("请输入邮箱"))
    card_dict = {"name": name,
                 "phone": phone,
                 "email": email}
    cardList.append(card_dict)
    print("%s新增成功" % name)


def show_all_card():
    print("---------开始查询名片------------")
    for card_dict in cardList:
        print("姓名是:%s,电话是:%s,邮箱是:%s" % (card_dict["name"], card_dict["phone"], card_dict["email"]))


def update_card():
    print("-----------开始更新名片-------------")
    query_name = str(input("请输入查询的用户名"))
    for card_dict in cardList:
        if card_dict["name"] == query_name:
            print("找到了:%s这个人,电话是:%s,邮箱是:%s" % (card_dict["name"], card_dict["phone"], card_dict["email"]))
            new_name = str(input("请输入要更改的姓名,回车不更改"))
            new_phone = str(input("请出入要更改的手机号,回车不更改"))
            new_email = str(input("请输入要更改的邮箱,回车不更改"))
            if new_name != '':
                card_dict["name"] = new_name
            if new_phone != '':
                card_dict["phone"] = new_phone
            if new_email != '':
                card_dict["email"] = new_email
            print("修改后的结果\r\n姓名是:%s,电话是:%s,邮箱是:%s" % (card_dict["name"], card_dict["phone"], card_dict["email"]))
            break
    else:
        print("没有找到%s" % query_name)
