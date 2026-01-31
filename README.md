# FastAPI Address Book Application

## Overview

This project is a FastAPI-based Address Book application.  
It allows API users to create, update, delete, and retrieve addresses.

Each address:
- Contains geographic coordinates (latitude and longitude)
- Is validated using Pydantic
- Is stored in an SQLite database

The application also supports retrieving addresses within a given distance from specified coordinates.

FastAPI’s built-in Swagger UI is used for testing the APIs (no separate GUI is required).

---

## Tech Stack

- Python 3
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

## Project Structure

fastapi-address-book/
|
|
|--- app/
| |
| |--- main.py
| |--- database.py
| |--- models.py
| |--- schemas.py
| |--- crud.py
|
|--- requirements.txt
|--- .gitignore
|--- README.md


---

## How to Execute the Application

### 
#1. Clone the repository
```bash
git clone https://github.com/Puneeth725/fastapi-address-book
cd fastapi-address-book


#2. Create and activate virtual environment

python -m venv venv
venv\Scripts\activate

#3. Install dependencies

pip install -r requirements.txt

#4. Run the application

uvicorn app.main:app --reload

#5. Open Swagger UI

http://127.0.0.1:8000/docs

# Available APIs

POST /addresses ? Create address

PUT /addresses/{id} ? Update address

DELETE /addresses/{id} ? Delete address

GET /addresses/nearby ? Retrieve nearby addresses



#Notes:

The SQLite database is created automatically when the application starts.

No separate GUI is required; FastAPI’s built-in Swagger UI is sufficient.




