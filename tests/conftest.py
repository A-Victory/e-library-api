from fastapi import HTTPException
import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app
from datetime import date
@pytest.fixture(scope="module")
def test_client():
    # Define mock data
    users = {
        1: {"id": 1, "name": "Alicia", "email": "alicia@example.com", "is_active": True},
        2: {"id": 2, "name": "Bob", "email": "bob@example.com", "is_active": True},
        3: {"id": 3, "name": "Charlie", "email": "charlie@example.com", "is_active": False},
    }
    books = {
        1: {"id": 1, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "is_available": True},
        2: {"id": 2, "title": "1984", "author": "George Orwell", "is_available": True},
        3: {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee", "is_available": False},
    }
    borrow_records = [
        {"id": 1, "user_id": 1, "book_id": 2, "borrow_date": date(2023, 1, 15), "return_date": None},
        {"id": 2, "user_id": 2, "book_id": 1, "borrow_date": date(2023, 2, 10), "return_date": date(2023, 2, 20)},
        {"id": 3, "user_id": 3, "book_id": 3, "borrow_date": date(2023, 3, 5), "return_date": None},
    ]
    
    with patch("app.routes.borrow.borrow_records", borrow_records), \
         patch("app.routes.book.books", books), \
         patch("app.routes.user.users", users), \
         patch("app.routes.borrow.borrow_helper") as mock_borrow_helper:

        # Mock BorrowBookHelper methods
        mock_borrow_helper.get_user_by_id = lambda user_id: users.get(user_id) or \
            HTTPException(status_code=404, detail=f"User with id {user_id} not found")
        mock_borrow_helper.get_book_by_id = lambda book_id: books.get(book_id) or \
            HTTPException(status_code=404, detail=f"Book with id {book_id} not found")
        mock_borrow_helper.is_book_available = lambda book_id: books[book_id]["is_available"]
        mock_borrow_helper.create_borrow_record = lambda user_id, book_id: {
            "id": len(borrow_records) + 1,
            "user_id": user_id,
            "book_id": book_id,
            "borrow_date": date.today(),
            "return_date": None,
        }
        
        mock_borrow_helper.check_availability = lambda book_id: (
            HTTPException(status_code=400, detail="Book is not available for borrowing") 
            if not books.get(book_id, {}).get("is_available", False) 
            else True
        )
        
        mock_borrow_helper.return_borrowed_book = lambda user_id, book_id: {
         "message": "Book returned successfully"
        } if any(record["user_id"] == user_id and record["book_id"] == book_id and record["return_date"] is None for record in borrow_records) else \
        HTTPException(status_code=404, detail="Borrow record not found")

        mock_borrow_helper.get_all_borrow_records = lambda: borrow_records
        mock_borrow_helper.get_user_borrow_records = lambda user_id: [
            record for record in borrow_records if record["user_id"] == user_id
        ]
        
        client = TestClient(app)
        yield client
