import CardTool

print("-----欢迎登陆名片管理系统-----")
print("1.输入1选择新增名片")
print("2.输入2查看所有名片")
print("3.输入3选择更改名片")
print("4.输入0退出系统")
while True:
    option = str(input("请输入你的选择:"))
    if option == "1":
        print("选择了新增")
        CardTool.insert_card()
    elif option == "2":
        print("选择了查询")
        CardTool.show_all_card()
    elif option == "3":
        print("选择了更新")
        CardTool.update_card()
    elif option == "0":
        print("选择了退出")
        break
    else:
        print("请出入正确的选择")
