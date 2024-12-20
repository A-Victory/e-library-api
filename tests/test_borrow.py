def test_borrow_book(test_client):
    # Borrow book as a user
    response = test_client.post("/borrow/2", json={"book_id": 1})  # Use json for POST request
    assert response.status_code == 200
    assert response.json()["message"] == "Book successfully borrowed"


def test_return_book(test_client):
    # Returning a borrowed book
    data = {
        "book_id": 2
    }
    response = test_client.post("/borrow/return/1", json={"book_id": 2})
    assert response.status_code == 200
    assert response.json()["message"] == "Book successfully returned"


def test__all_borrow_records(test_client):
    # Check all borrow records
    response = test_client.get("/borrow/")
    assert response.status_code == 200
    assert len(response.json()) == 3  # There are 3 borrow records in the mock


def test_get_user_borrow_records(test_client):
    # Check borrow records for a specific user (user_id=1)
    response = test_client.get("/borrow/1")
    assert response.status_code == 200
    assert len(response.json()) == 1  # Only one record for user_id 1
    assert response.json()[0]["user_id"] == 1


