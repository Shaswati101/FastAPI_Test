from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

users: List[User] = []   #List[User] denotes the type of the list 'user', meaning user will contain elements from the List[User]

@app.get("/greet/{user}")
def greet(user:str):
    return {"message": f"Don't be sorry. Be better.  ~{user}"}

@app.get("/users/")
def get_users():
    return users

@app.post("/users/")
def add_user(user: User):
    users.append(user)
    return {"message": f"User {user.name} added successfully"}

@app.get("/check_users/{email}")
def check_users(email: str):
    for user in users:
        if user.email == email:
            return user
    return {"error": "User does not exist"}
