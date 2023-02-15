from fastapi import FastAPI, Path
from typing import Optional

app=FastAPI()

students = {
    1: {
        "name":"john",
        "age": 17,
        "class":"year 5"
    }
}

@app.get("/")
def read_root():
    return{"Hello": "Word"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None), description="The ID of the student you want to view" ,gt=0, lt=3):
    return students[student_id]

@app.get("/get-by-name")
def get_student(name: Optional[str]):
    for students[student_id] in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return{"Data":"Not Found"}
