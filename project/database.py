from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import json

with open("config.json", "r") as config_file:
    config_data = json.load(config_file)

# PostgreSQL 연결 정보
DATABASE_USER = config_data["DATABASE_USER"]
DATABASE_PASSWORD = config_data["DATABASE_PASSWORD"]
DATABASE_HOST = config_data["DATABASE_HOST"]
DATABASE_PORT = config_data["DATABASE_PORT"]
DATABASE_NAME = config_data["DATABASE_NAME"]

# PostgreSQL 연결 문자열
SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# SQLAlchemy 엔진 생성
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

'''
## 테이블에 대한 모델을 정의할 필요가 없다고 판단됨
# 기존 테이블을 자동으로 매핑
Base = automap_base()
Base.prepare(engine, reflect=True)

# 각 테이블에 대한 모델 생성
F150_open_tbl = Base.classes.f150_open_tbl
'''

# SQLAlchemy 세션 생성
SessionLocal = Session(engine)
