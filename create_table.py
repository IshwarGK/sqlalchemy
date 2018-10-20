import datetime
import pymysql
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql+pymysql://ishwar:ishwar@localhost:3306/test_git")
Base = declarative_base()

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    class_name = Column(String(50))
    createdOn = Column(DateTime, default=datetime.datetime.now())
    modifiedOn = Column(DateTime, onupdate=datetime.datetime.now())


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    desciption = Column(String(100))
    author_name = Column(String(50))
    pages = Column(Integer)
    

Base.metadata.create_all(engine)

