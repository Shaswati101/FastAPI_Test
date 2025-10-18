from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Test(BaseModel):
    id: int
    subject: str
    teacher: str

tests: List[Test] = []


#FastAPI mainly works on the decorators making them APIs
@app.get("/")
def start_test():
    return {"message": "Welcome"}

@app.get("/get_test/{test_id}" , response_model=Test)
def get_test(test_id: int):
    for test in tests:
        if test.id == test_id:
            return test
    return {"error": "Test not found"}

@app.post("/add_test")
def add_test(test: Test):
    tests.append(test)
    return {"message": "Test added successfully"}

@app.put("/update_test/{test_id}")
def update_test(test_id: int, new_test: Test):
    for index, test in enumerate(tests):
        if test.id == test_id:
            test[index] = new_test
            return {"message": "Test Updated Successfully", "Updated Test": new_test}
    return {"error": "Test not found"}
