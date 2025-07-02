from pydantic import BaseModel
from typing import List

class Blog(BaseModel):
    title : str
    body : str

    class Config(): orm_model = True


class User(BaseModel):
    name : str
    email : str
    password : str

class showUser(BaseModel):
    name : str
    email : str
    blogs : List[Blog]
    class Config(): orm_model = True

class ShowBlog(BaseModel):
    title : str
    body : str
    creator : showUser

    class Config(): orm_model = True