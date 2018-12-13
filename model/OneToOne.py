from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Husband(Base):
    __tablename__ = "husband"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    job = Column(String, nullable=False)

    wife = relationship("Wife", backref="relate_husband", uselist=False)

    def __str__(self):
        return ("id:%s,name:%s,age:%s,job:%s") % (self.id, self.name, self.age, self.job)


class Wife(Base):
    __tablename__ = "wife"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    job = Column(String, nullable=False)
    husband_id = Column(Integer, ForeignKey("husband.id"), unique=True, nullable=False)

    def __str__(self):
        return ("id:%s,name:%s,age:%s,job:%s,husband_id:%s") % (self.id, self.name, self.age, self.job, self.husband_id)
