def test_create_user(test_client):
    new_user = {
        "name": "Alice",
        "email": "alice@example.com",
    }

    response = test_client.post("/users/", json=new_user)
    assert response.status_code == 201
    assert response.json()["name"] == "Alice"

def test_get_user_by_id(test_client):
    response = test_client.get("/users/4")
    assert response.status_code == 200
    assert response.json()["id"] == 4
    assert response.json()["name"] == "Alice"

def test_update_user(test_client):
    updated_user = {
        "name": "Alice Updated",
        "email": "alice.updated@example.com",
    }

    response = test_client.put("/users/1", json=updated_user)
    assert response.status_code == 200
    assert response.json()["name"] == "Alice Updated"

def test_deactivate_user(test_client):
    response = test_client.patch("/users/1/deactivate")
    assert response.status_code == 200
    assert response.json()["message"] == "user deactivated successfully"

def test_delete_user(test_client):
    response = test_client.delete("/users/1")
    assert response.status_code == 200
    assert response.json()["message"] == "user with id 1 deleted successfully"

def test_get_all_users(test_client):
    response = test_client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) > 0