from fastapi import FastAPI
from schemas import Blog

app = FastAPI()

@app.get('/')
def health():
    return "App is healthy"

@app.post('/blog')
def createBlog(request : Blog):
    return request