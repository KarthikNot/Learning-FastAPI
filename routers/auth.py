from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schemas, database, models
from hashing import verifyPassword

authRouter = APIRouter(tags = ['authentication'])

@authRouter.post('/login')
def login(req : schemas.Login, db : Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == req.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Credentials not found!')
    if not verifyPassword(user.password, req.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials!')
    # generate jwt and return this jwt token.
    return user

