from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    roll_no: int


@app.get("/")
def read_root():
    return {"msg": "Hello there"}


@app.get("/greet")
def greet_name(name: str, age: Optional[int]=None):
    return {"msg": f"Hello, {name} and your age is {age}!!"}


@app.post("/student", status_code=201)
def create_student(student: Student):
    return {
        "name": student.name,
        "age": student.age,
        "roll_no": student.roll_no
    }
