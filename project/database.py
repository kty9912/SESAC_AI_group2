from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

## In this file we will define logic for connecting the sqlalchmecy with database.

SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite_app.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args= {"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()