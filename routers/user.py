from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from hashing import encryptPassword
import schemas, models
from database import get_db

userRouter = APIRouter(tags=['users'])

@userRouter.post('/create-user/', status_code=status.HTTP_201_CREATED, response_model=schemas.showUser)
def createUser(req : schemas.User, db : Session = Depends(get_db)):
    newPassword = encryptPassword(req.password)
    newUser = models.User(name=req.name, email=req.email, password=newPassword)
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser
    # return {'message' : 'Successfully created a user!'}

@userRouter.get('/user/{id}', status_code=status.HTTP_200_OK, response_model=schemas.showUser)
def getUser(id : int, db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'User with {id} not found!')
    return user