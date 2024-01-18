from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationships
from database import Base

'''
class Post(Base):
    __tablename__ = "post"

    post_id = Column(Integer, primary_key = True, autoincrement = True)   # 기본키
    title = Column(Text, nullable = False)
    datetime_created = Column(DateTime(timezone=True), server_default=func.now())
    content = Column(Text, nullable = True)
    writer = Column(Text, nullable = False)
'''