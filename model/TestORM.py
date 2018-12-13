from model.User import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *

# 连接本地数据库,用一个字符串表示连接信息'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine("mysql+pymysql://root:root@localhost:3306/test")
# 创建会话
session = sessionmaker(engine)
# 创建session对象
DBSession = session()

# 新增数据到user表里面
# user = User(name='张三', age=24, sex=0, email='999@qq.com', address='杭州')
# # 添加到session
# DBSession.add(user)
# # 提交到数据库
# DBSession.commit()
# # 关闭session
# DBSession.close()

# 从数据库中查询,查询一条数据。
user = DBSession.query(User).filter(User.name == "哈哈哈").filter(User.id == 1).first()
if user is not None:
    print("type:", type(user))
    print("name:", user.name)

print("-------------------万恶的分隔符--------------------")
# 模糊查询
result = DBSession.query(User).filter(User.name.like("%三%"))
if result is not None:
    for user in result:
        print(user.__str__())

print("-------------------万恶的分隔符--------------------")
# 查询某个为null的字段
result = DBSession.query(User).filter(User.address.is_(None))
if result is not None:
    for user in result:
        print(user.__str__())

print("-------------------万恶的分隔符--------------------")
# in 查询
result = DBSession.query(User).filter(User.sex.in_([-1, 0]))
if result is not None:
    for user in result:
        print(user.__str__())

print("-------------------万恶的分隔符--------------------")
# not in
result = DBSession.query(User).filter(~User.sex.in_([-1, 0]))
if result is not None:
    for user in result:
        print(user.__str__())

print("-------------------万恶的分隔符--------------------")
# and 查询
result = DBSession.query(User).filter(User.name == "张三").filter(User.age == 24)
if result is not None:
    for user in result:
        print(user.__str__())

print("-------------------万恶的分隔符--------------------")
# or查询,倒叙
result = DBSession.query(User).filter(or_(User.name == "张三", User.name == "张三丰")).order_by(User.id.desc())
if result is not None:
    for user in result:
        print(user.__str__())

print("-------------------分页查询--------------------")
# 分页查询
result = DBSession.query(User).limit(2).offset(0)
print("第一页:")
if result is not None:
    for user in result:
        print(user.__str__())
result = DBSession.query(User).limit(2).offset(2)
print("第2页:")
if result is not None:
    for user in result:
        print(user.__str__())
result = DBSession.query(User).limit(2).offset(4)
print("第3页:")
if result is not None:
    for user in result:
        print(user.__str__())
result = DBSession.query(User).limit(2).offset(6)
print("第4页:")
if result is not None:
    for user in result:
        print(user.__str__())

# 更新数据库
# DBSession.query(User).filter(User.id == 6).update({"name": "我的名字呗更改了", "address": "我的住址也被更改了"})
# DBSession.commit()

# 删除某条数据
# DBSession.query(User).filter(User.id == 5).delete()
# DBSession.commit()
