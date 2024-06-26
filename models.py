from sqlalchemy import Column, TEXT, INT, BIGINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Test(Base):
   __tablename__ = "test"

   id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
   name = Column(TEXT, nullable=False)
   number = Column(INT, nullable=False)
   
   
class Test2(Base):
   __tablename__ = "test2"

   id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
   name = Column(TEXT, nullable=False)
   age = Column(INT, nullable=False)