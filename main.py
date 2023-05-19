from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import Role, User, UserUpdateRequest


app = FastAPI()


db: List[User] = [
    User(
        id=UUID("9935d0db-6983-4736-9e74-fd00d2bea118"),
        first_name="Ayo",
        last_name="Jo",
        gender="male",
        roles=[Role.user],
    ),
    User(
        id=UUID("20a5c597-d6c8-4024-b6e1-0f90f3ff11fb"),
        first_name="Maya",
        last_name="Ang",
        gender="male",
        roles=[Role.user, Role.super_admin],
    ),
]


@app.get("/")
def root():
    return {"Hello": "Joe"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    user.id = uuid4()
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db[:]:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404, detail=f"user with id {user_id} does not exist"
    )


@app.patch("/api/v1/users/{user_id}")
async def update_user(user: UserUpdateRequest, user_id: UUID):
    for saved_user in db:
        if saved_user.id == user_id:
            for key, value in saved_user.dict().items():
                if  hasattr(user, key) and getattr(user, key) is not None:
                    setattr(saved_user, key, value)
            return
    raise HTTPException(
        status_code=404, detail=f"user with id {user_id} does not exist"
    )
