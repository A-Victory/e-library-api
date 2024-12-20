from fastapi import APIRouter, HTTPException
from app.database import books
from app.models import Book, BookRequest, UpdateBookModel

router = APIRouter()

@router.post("/", response_model=Book, status_code=201)
def create_book(book: Book):
    if len(books) == 0:
        new_id = 1 
    else:
        new_id = max(books.keys()) + 1  

    book.id = new_id   

    # Check if the book already exists by both title and author
    existing_book = next((b for b in books.values() if b["title"] == book.title and b["author"] == book.author), None)
    if existing_book:
        raise HTTPException(status_code=400, detail="Book with this title and author already exists")

    books[new_id] = book.model_dump()
    book.id = new_id 

    return book


#get a book by id
@router.get("/{book_id}", response_model=Book, status_code=200)
def get_book_by_id(book_id: int):
    book = books.get(book_id)
    print(f"Book id: {book_id}")
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

#get all books
@router.get("/", response_model=list[Book], status_code=200)
def get_all_books():
    return list(books.values())

#update a book
@router.put("/{book_id}", response_model=Book, status_code=200)
def update_book(book_id: int, updated_book: UpdateBookModel):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    
    existing_book = books[book_id]

    updated_data = updated_book.model_dump(exclude_unset=True)
    for key, value in updated_data.items():
        existing_book[key] = value

    books[book_id] = existing_book
    return existing_book

#delete a book
@router.delete("/{book_id}", status_code=200)
def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    del books[book_id]
    return {"message": "Book deleted successfully"}

#mark a book as unavailable
@router.patch("/unavailable", status_code=200)
def set_book_unavailable(request: BookRequest):
    book_id = request.book_id
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    books[book_id]["is_available"] = False
    return {"message": "Book marked as unavailable"}

@router.post("/available", status_code=200)
def check_book_availability(request: BookRequest):
    book = request.book_id
    if book not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    if books[book]["is_available"]:
        return {"message": "Book is available for borrowing"}
    else:
        raise HTTPException(status_code=400, detail="Book is not available for borrowing")