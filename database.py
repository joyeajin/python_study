# from sqlalchemy import *
# from sqlalchemy.orm import sessionmaker

# DB_URL = 'mysql+pymysql://root:yeajin1009@localhost/goya_app_db'

# class engineconn:

#     def __init__(self):
#         self.engine = create_engine(DB_URL, pool_recycle = 500)

#     def sessionmaker(self):
#         Session = sessionmaker(bind=self.engine)
#         session = Session()
#         return session

#     def connection(self):
#         conn = self.engine.connect()
#         return conn



from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, declarative_base

# MySQL 연결 정보
DB_URL = 'mysql+pymysql://root:yeajin1009@localhost/goya_app_db'

# SQLAlchemy 엔진 생성
engine = create_engine(DB_URL, pool_recycle=500)

# 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 베이스 클래스 생성
Base = declarative_base()

# 예시 모델 정의
class Test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

# engineconn 클래스 사용 예시
class engineconn:
    def __init__(self):
        self.engine = engine

    def sessionmaker(self):
        return SessionLocal()

    def connection(self):
        return self.engine.connect()

# 데이터베이스에 데이터 추가하는 함수
def create_test(db_session, name: str, description: str):
    db_test = Test(name=name, description=description)
    db_session.add(db_test)
    db_session.commit()
    db_session.refresh(db_test)
    return db_test