import sys, pprint, random, shelve

pprint.pprint(sys.path)

a = {1, 2, 3, 4}
b = {2, 3, 4, 5, 6}
pprint.pprint(a.union(b))

pprint.pprint(random.uniform(0, 360))


def store_person(db):
    '''
    让用户输入用户并存入到shelve中
    :param db:
    :return:
    '''

    pid = input("Enter unique ID number")
    person = {}
    person["name"] = input("Enter name:")
    person["age"] = input("Enter age:")
    person["phone"] = input("Enter phone number:")
    db[pid] = person


def lookup_person(db):
    '''
    通过pid来查询用户
    :param db:
    :return:
    '''

    pid = input("Enter PID number")
    field = input("what would you like know (name, age or phone)")
    field = field.strip().lower()
    pprint.pprint(field.capitalize() + ":", db[pid][field])


def print_help():
    pprint.pprint("有效的操作命令如下:")
    pprint.pprint("store: Stores information about a person")
    pprint.pprint("lookup: find person by id number")
    pprint.pprint("quit: save change and exit")
    pprint.pprint("?: print this message")


def enter_command():
    cmd = input("enter ommand ? for help")
    cmd = cmd.strip().lower()
    return cmd


def main():
    database = shelve.open("/Users/zhankun/Desktop/database.dat")
    try:
        while True:
            cmd = enter_command()
            if cmd == "store":
                store_person(database)
            elif cmd == "lookup":
                lookup_person(database)
            elif cmd == "quit":
                return
            elif cmd == "?":
                print_help()
    finally:
        database.close()



