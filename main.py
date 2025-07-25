import models
from typing import List
from fastapi import FastAPI
from database import engine
from routers.blog import blogRouter
from routers.user import userRouter
from routers.auth import authRouter

models.base.metadata.create_all(engine)

app = FastAPI()

app.include_router(blogRouter)
app.include_router(userRouter)
app.include_router(authRouter)
