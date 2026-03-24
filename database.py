from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

MYSQL_USER = "admin"
MYSQL_PASSWORD = "Krish08021998"
MYSQL_HOST = "database-1.cfui8aucysuk.ap-south-1.rds.amazonaws.com"
MYSQL_PORT = 3306
MYSQL_DATABASE = "fastapi_db"

DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

engine = create_engine(DATABASE_URI)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()
