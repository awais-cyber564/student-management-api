# Student Management System API

## Overview
Student Management System API is a beginner-friendly backend project built with **Python** and **FastAPI**. It allows you to manage student data using CRUD operations and stores the data in a **JSON file**.

## Features
- Add a new student
- View all students
- Update student details
- Delete student
- Automatic Swagger UI documentation (`/docs`)
- JSON-based storage for simplicity

## Technologies Used
- Python 3
- FastAPI
- Uvicorn (ASGI server)
- JSON file storage

## Installation
1. Clone the repository:
```bash
git clone https://github.com/your-username/student-management-api.git
```

2. Navigate to the project folder:
```bash
cd student-management-api
```

3. Install dependencies:
```bash
pip install fastapi uvicorn
```

## Running the API
```bash
uvicorn main:app --reload
```
Open browser and go to: `http://127.0.0.1:8000/docs` to access **Swagger UI**.

## API Endpoints
| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | / | Home / API Status |
| GET | /students | Get all students |
| POST | /students | Add a new student |
| GET | /students/{id} | Get student by ID |
| PUT | /students/{id} | Update student by ID |
| DELETE | /students/{id} | Delete student by ID |

## Data Model
Each student record contains:
- `id` (int)
- `name` (str)
- `father_name` (str)
- `age` (int)
- `email` (str)
- `phone` (str)
- `course` (str)
- `address` (str)
- `admission_date` (str, auto-filled)

## Notes
- `students.json` stores all student data locally.
- Ensure `students.json` exists and is initialized with `[]` before running.

## Future Improvements
- Add login/authentication system
- Integrate with a proper database (SQLite/PostgreSQL)
- Connect with a frontend UI
- Deploy to cloud platforms

## Author
**Awais**

---
*This project is designed for learning FastAPI and basic CRUD operations.*

