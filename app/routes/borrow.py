from fastapi import APIRouter, HTTPException
from app.database import borrow_records
from app.models import BookRequest, BorrowRecord
from app.utils import borrow_helper
from datetime import date

router = APIRouter()

@router.post("/{user_id}", status_code=200)
def borrow_book(user_id: int, borrow_request: BookRequest):
    book_id = borrow_request.book_id
    borrow_helper.get_user_by_id(user_id)
    borrow_helper.get_book_by_id(book_id)
    borrow_helper.is_active_user(user_id)
    borrow_helper.is_book_available(book_id)
    borrow_helper.has_user_already_borrowed(user_id, book_id)
    record = borrow_helper.create_borrow_record(user_id, book_id)
    return {"message": "Book successfully borrowed", "record": record}

@router.post("/return/{user_id}", status_code=200)
def return_book(user_id: int, return_request: BookRequest):
    book_id = return_request.book_id
    record = borrow_helper.return_borrowed_book(user_id, book_id)
    return {"message": "Book successfully returned", "record": record}


@router.get("/", status_code=200, response_model=list[BorrowRecord])
def get_all_borrow_records():
    return borrow_records

@router.get("/{user_id}", status_code=200)
def get_user_borrow_records(user_id: int):
    borrow_helper.get_user_by_id(user_id)
    records = [record for record in borrow_records if record["user_id"] == user_id]
    return records


