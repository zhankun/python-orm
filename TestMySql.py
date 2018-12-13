import pymysql


def connect_db():
    print("------开始连接mysql数据库-------")
    db = pymysql.connect("localhost", "root", "root", "test")
    # cursor = db.cursor()
    print("连接成功")
    return db


def create_table(db):
    """
    生成表
    :param db:
    :return:
    """

    # 解决局部变量无法自动提示问题
    assert isinstance(db, pymysql.Connect())
    cursor = db.cursor()
    cursor.execute("drop table if exists student")
    sql = """CREATE TABLE Student (
            ID CHAR(10) NOT NULL,
            Name CHAR(8),
            Grade INT )"""
    cursor.execute(sql)


def insert_db():
    """
    向数据库中插入数据
    :return:
    """

    db = connect_db()
    cursor = db.cursor()
    sql = "insert into student values ('1','张三',70)," \
          "('2','李四',76)," \
          "('3','王五',50)," \
          "('4','赵六',94)"
    cursor.execute(sql)
    # 提交事务
    db.commit()


def query_db():
    """
    查询数据库
    :return:
    """

    db = connect_db()
    # 获取操作数据库的游标
    cursor = db.cursor()
    sql = "select * from student"
    # 执行sql语句
    cursor.execute(sql)
    # 获取操作结果
    result = cursor.fetchall()
    # 循环遍历结果集
    for row in result:
        id = row[0]
        name = row[1]
        grade = row[2]
        print("id是:%s,姓名是:%s,分数是:%s" % (id, name, grade))


def update_db(grade, id):
    """
    更新数据库
    :return:
    """

    db = connect_db()
    cursor = db.cursor()
    update_sql = "update student set grade = %s where id = %s" % (grade, id)
    cursor.execute(update_sql)
    db.commit()


# db = connect_db()
# create_table(db)
#insert_db()
#query_db()
update_db(100, 3)
