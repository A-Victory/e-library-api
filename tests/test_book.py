# tests/test_book.py

def test_create_book(test_client ):
    # Mocking database behavior for book creation
    new_book = {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinge",
    }

    response = test_client.post("/books/", json=new_book)
    assert response.status_code == 201
    assert response.json()["title"] == "The Catcher in the Rye"

def test_get_book_by_id(test_client ):
    # Mocking the retrieval of a book by ID
    
    response = test_client.get("/books/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["title"] == "The Catcher in the Rye"

def test_get_all_books(test_client ):
    # Mocking retrieval of all books
    
    response = test_client.get("/books/")
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_update_book(test_client ):
    # Mocking book update
    updated_book = {
        "title": "The Catcher in the Rye - Updated",
        "author": "J.D. Salinger",
    }
   
    response = test_client.put("/books/1", json=updated_book)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["title"] == "The Catcher in the Rye - Updated"
    assert response_data["author"] == "J.D. Salinger"
    assert response_data["is_available"] is True

def test_set_book_unavailable(test_client):
    # Mocking marking book as unavailable
    response = test_client.patch("/books/unavailable", json={"book_id": 1})
    assert response.status_code == 200
    assert response.json()["message"] == "Book marked as unavailable"

def test_delete_book(test_client):
    # Mocking book deletion

    response = test_client.delete("/books/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Book deleted successfully"


def test_check_availability(test_client):
    # Trying to check if a book is available (book_id = 3 which is unavailable in our mock data)
    response = test_client.post("/books/available", json={"book_id": 3})
    
    print (response.json())
    # Assert that the status code is 400 since the book is unavailable
    assert response.status_code == 400
    assert response.json()["detail"] == "Book is not available for borrowing"
