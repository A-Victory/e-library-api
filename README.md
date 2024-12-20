# E-Library API System

## Overview

The E-Library API System is a FastAPI-based application designed to manage an online library system. It provides endpoints for users to borrow and return books, manage user information, and track book availability, based for my ALTSCHOOL second sememster project

This API system facilitates:

- User management (creating, deactivating, and updating user profiles),
- Book management (CRUD operations and availability status updates),
- Borrowing and returning books (ensuring books are available and properly tracked),
- Tracking borrowing records (view records per user and all borrowing activities).


## Features

- **User Management**: Create, update, delete, and retrieve users.
- **Book Management**: Create, update, delete, and retrieve books.
- **Borrow Management**: Borrow and return books, check borrow records.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/A-Victory/e-library-api.git
    cd e-library-api
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the FastAPI server:
    ```sh
    uvicorn app.main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## Project Structure

```plaintext
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── book.py
│   │   ├── borrow.py
│   ├── utils.py
├── tests
│   ├── __init__.py
│   ├── test_user.py
│   ├── test_book.py
│   ├── test_borrow.py
│   ├── conftest.py
├── requirements.txt
└── README.md
```

## API Endpoints

### Users

- **POST /users/**: Create a new user.
- **GET /users/{user_id}**: Get a user by ID.
- **GET /users/**: Get all users.
- **PUT /users/{user_id}**: Update a user.
- **DELETE /users/{user_id}**: Delete a user.
- **PATCH /users/{user_id}/deactivate**: Deactivate a user.

### Books

- **POST /books/**: Create a new book.
- **GET /books/{book_id}**: Get a book by ID.
- **GET /books/**: Get all books.
- **PUT /books/{book_id}**: Update a book.
- **DELETE /books/{book_id}**: Delete a book.
- **PATCH /books/unavailable**: Mark a book as unavailable.
- **POST /books/available**: Check if a book is available.

### Borrow

- **POST /borrow/{user_id}**: Borrow a book.
- **POST /borrow/return/{user_id}**: Return a borrowed book.
- **GET /borrow/**: Get all borrow records.
- **GET /borrow/{user_id}**: Get borrow records for a specific user.

## Testing

To run the tests for the E-Library API System, follow these steps:

1. Ensure you have the necessary dependencies installed:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the tests using `pytest`:
    ```sh
    pytest
    ```

The tests are located in the `tests` directory and cover various aspects of the application, including user management, book management, and borrow management.

