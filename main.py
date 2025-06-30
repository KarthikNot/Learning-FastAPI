from fastapi import FastAPI
from schemas import Blog
from database import engine
import models

models.base.metadata.create_all(engine)

app = FastAPI()

@app.get('/')
def health():
    return "App is healthy"

@app.post('/blog')
def createBlog(request : Blog):
    return request