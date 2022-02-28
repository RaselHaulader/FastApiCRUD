from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name":'Rasel',
        "age": 24,
        "year": 'Honors'
    }
}
# make class template to post data 
class Student(BaseModel):
    name : str
    age: int
    year : str

# update student 
class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None


@app.get("/")
def index():
    return students

# get value with params ex - url/id
@app.get("/student/{id}")
def get_student(id : int = Path(None, description="The ID of the student you want to view", gt =0, lt=3)):
    return students[id]

#get value by params here params value automaticely set in name // http://127.0.0.1:8000/get-by-name?name=Rasel
@app.get("/get-by-name")
# here use optional param its means if you don't set any param its accepted and * its use to accept multiple params with Optional 
def get_student(*,name: Optional[str] = None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
        return {"data":"Student Not found"}

# create data 
@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students:
     return {"Error": "student exist"}

    students[student_id] = student
    return students[student_id]

# update student
@app.put("/update-student/{student_id}")
def update_student(student_id : int, student : UpdateStudent):
     if student_id not in students:
         return {"Error": "Student not found"}
    
    #  dot notation not working for hardcoded data
    #  if student.name != None:
    #      students[student_id].name = student.name
     if student.name != None:
         students[student_id]["name"] = student.name
     
     if student.age != None:
         students[student_id]["age"] = student.age
     
     if student.year != None:
         students[student_id][year] = student.year

     return students[student_id]

# delete data 
@app.delete("/delete-student/{id}")
def delete_student(id : int):
    if id not in students:
        return {"Error":"Student Not Found"}

    del students[id]
    return {"Message": "Delete successfull"}