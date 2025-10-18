from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/greet/{user}")
def greet(user:str):
    return {"message": f"Don't be sorry. Be better.  ~{user}"}