from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
import json

app = FastAPI() 

#load_user()

# class User(BaseModel):
#     #id: int
#     name: str
#     email: str
#     password: str
    

# users: List[User] = [] #List[User] denotes the type of the list 'user', meaning user will contain elements from the List[User]


@app.get("/greet/{user}")
def greet(user:str):
    return {"message": f"Don't be sorry. Be better. ~{user}"}

# @app.get("/users/")
# def get_users():
#     return users

# @app.post("/users/")
# def add_user(user: User):
#     users.append(user)
#     #Instead of appending to a list, you can also save to a file here.
#     return {"message": f"User {user.name} added successfully"}

# @app.get("/check_users/{email}")
# def check_users(id: int, password: str):
#     for user in users:
#         if user.id == id and user.password == password:
#             return user.email
#         else:
#             return {"error": "User ID or password is incorrect"}
#     return {"error": "User does not exist"}


@app.get("/give_name_password/", response_class=HTMLResponse)
def give_name_password(request:Request):
    html_content = """
    <html>
        <head>
            <title>Enter Name and Password</title>
        </head>
        <body>
            <form action="/get_email/" method="post">
                Name: <input type="text" name="name"><br>
                Password: <input type="password" name="password"><br>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """
    return html_content


@app.post("/get_email/")
def get_user(request: Request, name: str = Form(...), password: str = Form(...)):
    # request.session["user"] = {"name": name}
    with open("users.txt", "r", encoding="utf-8") as f:
        data = f.read()
#    database = file("users.txt", "r")
        if data.split(",")[1] == name and data.split(",")[2] == password:
            return data.split(",")[0]
        else:
            return "Invalid Credentials"