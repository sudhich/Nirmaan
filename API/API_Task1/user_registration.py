#python -m pip install email-validator
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field, SecretStr

app = FastAPI(title="User Registration API")

# Temporary in-memory storage
registered_users = []


# Pydantic validation model
class User(BaseModel):
    username: str = Field(min_length=4)
    email: EmailStr
    password: SecretStr = Field(min_length=8)


# POST endpoint: Register user
@app.post("/register")
def register_user(user: User):

    # Check duplicate email
    for existing_user in registered_users:
        if existing_user["email"] == str(user.email):
            return {
                "message": "Email already registered"
            }

    # Store user information
    registered_users.append({
        "username": user.username,
        "email": str(user.email),
        "password": user.password
    })

    return {
        "message": "User registered successfully!",
        "username": user.username,
        "email": str(user.email)
    }


# GET endpoint: Display registered users
@app.get("/users")
def get_users():

    return {
        "total_users": len(registered_users),
        "users": [
            {
                "username": user["username"],
                "email": user["email"]
            }
            for user in registered_users
        ]
    }


# {
#     "username": "sudhir",
#     "email": "sudhir@gmail.com",
#     "password": "python123",
#     "username": "sudhir2",
#     "email": "sudhir2@gmail.com",
#     "password": "python1234"
# }