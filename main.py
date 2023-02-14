from fastapi import FastAPI, Path

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

@app.get("/get_all_students")
def get_all_stud():
    return
