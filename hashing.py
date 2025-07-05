from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated = 'auto')

def encryptPassword(password : str):
    return pwd_cxt.hash(password)

def verifyPassword(hashedPassword : str, plainPassword : str):
    return pwd_cxt.verify(plainPassword, hashedPassword)