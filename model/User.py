from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    # 表名称
    __tablename__ = 'user'
    # id字段
    id = Column(Integer, primary_key=True, autoincrement=True)
    # name字段
    name = Column(String(length=255), nullable=False)
    # age字段
    age = Column(Integer, default=0)
    # 性别
    sex = Column(Integer, default=-1, nullable=False)
    # 邮箱
    email = Column(String(length=255))
    # 住址
    address = Column(String(length=255))

    def __str__(self):
        return ("编号:%s,姓名:%s,年龄:%s,性别:%s,邮箱:%s,住址:%s") % \
               (self.id, self.name, self.age, self.sex, self.email, self.address)
