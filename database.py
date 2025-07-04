from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_DATABASE_URL = 'sqlite:///./blog.db'

engine  = create_engine(SQL_DATABASE_URL, connect_args={'check_same_thread' : False})
base = declarative_base()

SessionLocal = sessionmaker(bind = engine, autocommit = False, autoflush = False)

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()