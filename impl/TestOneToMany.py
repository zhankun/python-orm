from model.OneToMany import Parent
from model.OneToMany import Child
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *

# 连接本地数据库,用一个字符串表示连接信息'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine("mysql+pymysql://root:root@localhost:3306/test")
# 创建会话
session = sessionmaker(engine)
# 创建session对象
DBSession = session()

# 新增数据
# parent = Parent(name="李四", age=46, sex=1)
# child1 = Child(name="李小三")
# child2 = Child(name="李小四")
# child3 = Child(name="李小五")
# parent.child = [child1, child2, child3]
# DBSession.add(parent)
# DBSession.commit()

# 查询某个parent对应的child
result = DBSession.query(Parent).filter(Parent.name == "张三").first().child
for child in result:
    print(child)

# 知道某个child，查找该child属于哪个parent
result = DBSession.query(Child).filter(Child.name == "李小三").first().relate_parent
print(result)

# 更新某个child

