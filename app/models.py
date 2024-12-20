from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import date

class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr
    is_active: Optional[bool] = True
    
class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    is_available: Optional[bool] = True
    
class BorrowRecord(BaseModel):
    id: int
    user_id: int
    book_id: int
    borrow_date: date
    return_date: Optional[date] = None
    

class BookRequest(BaseModel):
    book_id: int
    
class UpdateBookModel(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    is_available: Optional[bool] = None