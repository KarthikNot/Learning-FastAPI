from database import base
from sqlalchemy import Column, Integer, String


class Blog(base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
 