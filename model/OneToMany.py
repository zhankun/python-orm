from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


# 一对多，父母对多个孩子
class Parent(Base):
    __tablename__ = "parent"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    sex = Column(Integer, nullable=False)

    # relate_parent,当已知子类时，调用这个可以获取到父类
    # child，已知父类，调用这个可以获得父类下面所有的子类
    # 这两个名字都是可以自定义的.Child必须对应子的名字
    child = relationship("Child", backref='relate_parent')

    def __str__(self):
        return ("id:%s,name:%s,age:%s,sex:%s") % (self.id, self.name, self.age, self.sex)


class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey('parent.id'))

    # father = relationship("Parent", backref="child", uselist=False)

    def __str__(self):
        return ("id:%s,name:%s,parent_id:%s") % (self.id, self.name, self.parent_id)
