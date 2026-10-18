from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Library API")

class BookCreate(BaseModel):      
    title: str
    author: str
    year: int | None = None

class Book(BookCreate):           
    id: int

class BookUpdate(BaseModel):      
    title: str | None = None
    author: str | None = None
    year: int | None = None

books: dict[int, Book] = {}   
next_id = 1                  
@app.get("/books", response_model=list[Book])
def list_books():
    return list(books.values())


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(data: BookCreate):
    global next_id
    book = Book(id=next_id, **data.model_dump())
    books[next_id] = book
    next_id += 1
    return book

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = books.get(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.patch("/books/{book_id}", response_model=Book)
def update_book(book_id: int, data: BookUpdate):
    book = books.get(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    changes = data.model_dump(exclude_unset=True)
    updated = book.model_copy(update=changes)
    books[book_id] = updated
    return updated

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    del books[book_id]