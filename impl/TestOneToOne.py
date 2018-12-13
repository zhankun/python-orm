from model.OneToOne import Husband, Wife
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *

# 连接本地数据库,用一个字符串表示连接信息'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine("mysql+pymysql://root:root@localhost:3306/test")
# 创建会话
session = sessionmaker(engine)
# 创建session对象
DBSession = session()



# 新增数据
# husband1 = Husband(name="张三", age=29, job="程序猿")
# wife1 = Wife(name="张翠花", age=32, job="全职太太")
# husband1.wife = wife1
# husband2 = Husband(name="李四", age=32, job="滴滴司机")
# wife2 = Wife(name="李菜花", age=31, job="商场导购")
# husband2.wife = wife2
# husband3 = Husband(name="李小二", age=40, job="面馆老板")
# wife3 = Wife(name="王婆", age=42, job="面馆老板娘")
# husband3.wife = wife3
#
# batch_list = [husband1, husband2, husband3]
# # 批量insert
# DBSession.add_all(batch_list)
# DBSession.commit()
# DBSession.bulk_save_objects(batch_list)


result = DBSession.query(Husband).filter(Husband.name.like("%李%"))
if result is not None:
    for husband in result:
        print(husband.__str__())
        print(husband.wife)

print("--------分割线----------")
result = DBSession.query(Wife).filter(Wife.name.like("%花%"))
if result is not None:
    for wife in result:
        print(wife.relate_husband)

