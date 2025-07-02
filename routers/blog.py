from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
import schemas, models
from database import get_db
from typing import List

blogRouter = APIRouter(tags=['blogs'])

@blogRouter.post('/blog', status_code=status.HTTP_201_CREATED )
def createBlog(request : schemas.Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@blogRouter.get('/blog', status_code = status.HTTP_200_OK, response_model = List[schemas.ShowBlog] )
def getBlogs(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@blogRouter.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog )
def getBlogById(id : int, res : Response, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found.")
    return blog

@blogRouter.delete('/delete-blog/{id}', status_code=status.HTTP_200_OK )
def deleteBlog(id : int, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Blog with id {id} not found!')
    blog.delete(synchronize_session = False)
    db.commit()

    return 'Done'

@blogRouter.put('/update-blog/{id}', status_code = status.HTTP_202_ACCEPTED )
def updateBlog(id : int, req : schemas.Blog, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with id {id} not found!')
    blog.update(req.model_dump())
    db.commit()
    return {'message' : f'Successfully updated the Blog with id {id}'}