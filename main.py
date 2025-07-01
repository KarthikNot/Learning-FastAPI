from fastapi import FastAPI, Depends, status, Response, HTTPException
from schemas import Blog
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import models

models.base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

app = FastAPI()

@app.get('/')
def health():
    return "App is healthy"

@app.post('/blog', status_code=status.HTTP_201_CREATED)
def createBlog(request : Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog', status_code = status.HTTP_200_OK)
def getBlogs(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def getBlogById(id : int, res : Response, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found.")
    return blog

@app.delete('/delete-blog/{id}', status_code=status.HTTP_200_OK)
def deleteBlog(id : int, db : Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session = False)
    db.commit()

    return 'Done'