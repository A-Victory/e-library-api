from fastapi import APIRouter, HTTPException
from app.database import users
from app.models import User

router = APIRouter()

@router.post("/", response_model=User, status_code=201)
def create_user(user: User):
    # Auto-assign the id
    if len(users) == 0:
        new_id = 1  # Start from 1 if there are no users
    else:
        new_id = max(users.keys()) + 1  # Increment the highest existing id

    user.id = new_id  # Assign the new id to the user

    # Check if user already exists (optional, based on email or other unique field)
# Check if the email already exists by iterating over user values
    if any(existing_user["email"] == user.email for existing_user in users.values()):
        raise HTTPException(status_code=400, detail="User with this email already exists")
    users[user.id] = user.model_dump()
    return user

@router.get("/{user_id}", response_model=User, status_code=200)
def get_user_by_id(user_id: int):
    user = users.get(user_id)
    print(users)
    print(f"{user_id}")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=list[User], status_code=200)
def get_all_users():
    return list(users.values())


@router.put("/{user_id}", response_model=User, status_code=200)
def update_user(user_id: int, updated_user: User):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = updated_user.model_dump()
    return updated_user

@router.delete("/{user_id}", status_code=200)
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return {"message": f"user with id {user_id} deleted successfully"}

@router.patch("/{user_id}/deactivate", status_code=200)
def deactivate_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id]["is_active"] = False
    return {"message": "user deactivated successfully"}