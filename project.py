from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from  database import get_db, engine
import model

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    publish_date: str


@app.post("/books")
def create_book(book: Book, db: Session=Depends(get_db)):
    new_book = model.Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@app.get("/books")
def get_books(db: Session=Depends(get_db)):
    books = db.query(model.Book).all()
    return books

