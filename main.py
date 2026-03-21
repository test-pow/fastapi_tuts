from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
def read_root():
    return {"msg": "Hello there"}


@app.get("/greet")
def greet_name(name: str, age: Optional[int]=None):
    return {"msg": f"Hello, {name} and your age is {age}!!"}
