from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
import json
import os

with open(os.path.join("config.json"), "r") as config_file:
    config_data = json.load(config_file)

# PostgreSQL 연결 정보
DATABASE_USER = config_data["DATABASE_USER"]
DATABASE_PASSWORD = config_data["DATABASE_PASSWORD"]
DATABASE_HOST = config_data["DATABASE_HOST"]
DATABASE_PORT = config_data["DATABASE_PORT"]
DATABASE_NAME = config_data["DATABASE_NAME"]

# PostgreSQL 연결 문자열
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# SQLAlchemy 엔진 생성
'''
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
'''


engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL
)



# SQLAlchemy 세션 생성
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)