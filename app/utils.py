from app.database import users, books, borrow_records
from fastapi import HTTPException
from datetime import date

class BorrowBookHelper:

    @staticmethod
    def get_user_by_id(user_id: int):
        print("Accessing mocked users:", users)  # Print users to verify mock
        user = users.get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
        return user

    
    @staticmethod
    def get_book_by_id(book_id: int):
        book = books.get(book_id)
        if not book:
            print("Could not find book with id: {}".format(book_id))
            raise HTTPException(status_code=404, detail=f"book with id {book_id} not found")
        return book
    
    @staticmethod
    def is_active_user(user_id: int):
        user = BorrowBookHelper.get_user_by_id(user_id)
        if not user["is_active"]:
            print("User is not active")
            raise HTTPException(status_code=400, detail="User's account is not active")
        return True
    
    @staticmethod        
    def is_book_available(book_id: int):
        book = BorrowBookHelper.get_book_by_id(book_id)
        if not book["is_available"]:
            print("Book is not available for borrowing")
            raise HTTPException(status_code=400, detail="Book is not available for borrowing")
        return True
    
    @staticmethod
    def create_borrow_record(user_id: int, book_id: int):
        record_id = len(borrow_records) + 1
        new_record = {
            "id": record_id,
            "user_id": user_id,
            "book_id": book_id,
            "borrow_date": date.today(),
            "return_date": None,
        }
        borrow_records.append(new_record)
        
        books[book_id]["is_available"] = False
        return new_record
    
    @staticmethod
    def return_borrowed_book(user_id: int, book_id: int):
        record = next((r for r in borrow_records if r["user_id"] == user_id and r["book_id"] == book_id and r["return_date"] is None), None)
        
        if not record:
            raise HTTPException(status_code=404, detail="Borrowed record not found")
        if record["return_date"] is not None:
            raise HTTPException(status_code=400, detail="Borrowed book already returned")
        
        record["return_date"] = date.today()
        
        # Update book availability
        books[book_id]["is_available"] = True
        
        return record
    
    @staticmethod
    def has_user_already_borrowed(user_id: int, book_id: int):
        for record in borrow_records:
            if record["user_id"] == user_id and record["book_id"] == book_id and record["return_date"] is None:
                raise HTTPException(status_code=400, detail="User has already borrowed this book")
        return False
    
    @staticmethod
    def check_availability(book_id: int):
        book = BorrowBookHelper.get_book_by_id(book_id)
        print(f"{book}")
        if not book["is_available"]:
            print("Book is not available for borrowing")
            raise HTTPException(status_code=400, detail="Book is not available for borrowing")
        return True
    
borrow_helper = BorrowBookHelper()