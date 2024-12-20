from datetime import date

users = {} #Key: user_id, Value: user dictionary
books = {} #Key: book_id, Value: book dictionary
borrow_records = [] # List of book records for borrowed books

# Dummy Users Data
users = {
    1: {"id": 1, "name": "John", "email": "john@example.com", "is_active": True},
    2: {"id": 2, "name": "Eve", "email": "eve@example.com", "is_active": True},
    3: {"id": 3, "name": "Sam", "email": "sam@example.com", "is_active": False},  # Inactive user
    4: {"id": 4, "name": "Nina", "email": "nina@example.com", "is_active": True},
}

# Dummy Books Data
books = {
    1: {"id": 1, "title": "Brave New World", "author": "Aldous Huxley", "is_available": True},  # Available
    2: {"id": 2, "title": "Moby Dick", "author": "Herman Melville", "is_available": False},  # Unavailable
    3: {"id": 3, "title": "The Hobbit", "author": "J.R.R. Tolkien", "is_available": True},  # Available
    4: {"id": 4, "title": "Fahrenheit 451", "author": "Ray Bradbury", "is_available": True},  # Available
}

# Dummy borrow records
borrow_records.append({"id": 1, "user_id": 1, "book_id": 3, "borrow_date": date(2023, 5, 1), "return_date": None})
borrow_records.append({"id": 2, "user_id": 2, "book_id": 4, "borrow_date": date(2023, 6, 10), "return_date": None})
borrow_records.append({"id": 3, "user_id": 4, "book_id": 1, "borrow_date": date(2023, 7, 15), "return_date": date(2023, 8, 5)})
borrow_records.append({"id": 4, "user_id": 1, "book_id": 2, "borrow_date": date(2023, 9, 10), "return_date": None})
