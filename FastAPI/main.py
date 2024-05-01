from fastapi import FastAPI, HTTPException
from models import User, Gender, Role, UserUpdate
from typing import List
from uuid import uuid4, UUID

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name = "Sabiha",
        last_name = "Siraj",
        middle_name = "Binte",
        gender = Gender.female,
        roles = [Role.admin, Role.student]
        ),
    User(
        id=uuid4(),
        first_name = "Md. Jakaria",
        last_name = "Jihad",
        middle_name = "Hossain",
        gender = Gender.male,
        roles = [Role.admin, Role.user]
        ),
    User(
        id=uuid4(),
        first_name = "Dummy",
        last_name = "To be",
        middle_name = "Deleted",
        gender = Gender.male,
        roles = [Role.user]
        )
]

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.get("/api/v1/users/{user_id}")
async def fetch_single_users(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(
        status_code=404,
        detail=f"User {user_id} not found!"
    )


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code= 404,
        detail= f"User with id: {user_id} does not exists."
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdate, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} can't be found and updated."
    )