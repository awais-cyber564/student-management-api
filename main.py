from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Optional
import json
import os
from datetime import datetime

# ------------------ App Initialization ------------------

app = FastAPI(
    title="Student Management System API",
    description="Beginner friendly FastAPI project with JSON storage",
    version="1.0"
)

DATA_FILE = "students.json"

# ------------------ Helper Functions ------------------

def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)

# ------------------ Pydantic Models (SIMPLE) ------------------

class Student(BaseModel):
    id: int
    name: str
    father_name: str
    age: int
    email: EmailStr
    phone: str
    course: str
    address: str
    admission_date: str = datetime.now().strftime("%Y-%m-%d")

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    father_name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    course: Optional[str] = None
    address: Optional[str] = None

# ------------------ Routes ------------------

@app.get("/")
def home():
    return {"message": "Student Management System API is running successfully"}

# ➕ Add New Student
@app.post("/students", response_model=Student)
def add_student(student: Student):
    students = load_students()

    for s in students:
        if s["id"] == student.id:
            raise HTTPException(status_code=400, detail="Student ID already exists")

    students.append(student.dict())
    save_students(students)
    return student

# 📄 Get All Students
@app.get("/students", response_model=List[Student])
def get_all_students():
    return load_students()

# 🔍 Get Student by ID
@app.get("/students/{student_id}", response_model=Student)
def get_student_by_id(student_id: int):
    students = load_students()

    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")

# ✏️ Update Student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_data: StudentUpdate):
    students = load_students()

    for student in students:
        if student["id"] == student_id:

            if updated_data.name:
                student["name"] = updated_data.name
            if updated_data.father_name:
                student["father_name"] = updated_data.father_name
            if updated_data.age:
                student["age"] = updated_data.age
            if updated_data.email:
                student["email"] = updated_data.email
            if updated_data.phone:
                student["phone"] = updated_data.phone
            if updated_data.course:
                student["course"] = updated_data.course
            if updated_data.address:
                student["address"] = updated_data.address

            save_students(students)
            return {
                "message": "Student updated successfully",
                "updated_student": student
            }

    raise HTTPException(status_code=404, detail="Student not found")

# ❌ Delete Student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    students = load_students()

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            return {"message": "Student deleted successfully"}

    raise HTTPException(status_code=404, detail="Student not found")
