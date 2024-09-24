# python3 -m venv .venv
# .\.venv\bin\activate
# uvicorn app:app -- reload

from fastapi import FastAPI, HTTPException 
from uuid import UUID, uuid4 # Id generator randomic
from typing import List # Optional data type
from models import User, Role # Import the User model


app = FastAPI() # Create the FastAPI app

db: List[User] = [  # Create list to store the users
    User( id=UUID("382a8b84-f104-4397-b9b5-4bac33e7ecb1"),
          first_name="Caroline", 
          last_name="Camargo", 
          email="email@gmail.com", 
          role=[Role.role_1]
    ),
    User( id=UUID("3c28bb78-3d12-45d2-9e9f-3e3130bf0b9e"),
          first_name="Cynthia", 
          last_name="Zanoni", 
          email="email@gmail.com", 
          role=[Role.role_2]
    ),
    User( id=UUID("82ce329e-3149-4304-b9fb-b6f2de92ac77"),
          first_name="Camila", 
          last_name="Silva", 
          email="email@gmail.com", 
          role=[Role.role_3]
    ),
]

@app.get("/") # Define the route
async def root():
    return {"message": "Hello World! Hello Womakers"}


@app.get("/api/users") 
async def get_users():
    return db

@app.get("/api/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "User not found"}

@app.post("/api/users")
async def add_user(user: User):
    '''
    Add a new user to the database
    - **id**: UUID - Id generator randomic
    - **first_name**: string - First name of the user
    - **last_name**: string - Last name of the user
    - **email**: string - Email of the user
    - **role**: role - List of roles
    '''
    db.append(user)
    return {"id": user.id}

@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return 
        
    raise HTTPException(
        status_code=404, 
        detail=f"User with id {id} not found"
    )
