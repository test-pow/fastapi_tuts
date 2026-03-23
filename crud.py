from fastapi import FastAPI, HTTPException
from starlette import status
from pydantic import BaseModel

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publication_date": "1960-07-11"
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "publication_date": "1949-06-08"
    },
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publication_date": "1925-04-10"
    },
    {
        "id": 4,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publication_date": "1813-01-28"
    },
    {
        "id": 5,
        "title": "Moby-Dick",
        "author": "Herman Melville",
        "publication_date": "1851-10-18"
    }
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    publication_date: str


class BookUpdate(BaseModel):
    title: str
    author: str
    publication_date: str



@app.get("/books", status_code=status.HTTP_200_OK)
def get_all_books():
    return books


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.post("/books/create", status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    new_book = book.model_dump()
    books.append(new_book)
    return new_book


@app.put("/books/update/{book_id}", status_code=status.HTTP_200_OK)
def update_book(book_id: int, book_update: BookUpdate):
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update.title
            book["author"] = book_update.author
            book["publication_date"] = book_update.publication_date
            return {"msg": "Book updated successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.delete("/books/delete/{book_id}", status_code=status.HTTP_200_OK)
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"msg": "Book deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
