from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel
from http.client import HTTPException
from fastapi import HTTPException, Body, responses, status

app = FastAPI()

users = []

class User(BaseModel):
    id : int = None
    username: str = 'John Doe'
    age : int = None

@app.get('/users')
async def all_users():
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=5, max_length=50, description='Enter username', example='UrbanUser')], age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    user = User()
    user.id = len(users) + 1
    user.username = username
    user.age = age
    users.append(user)
    return user

@app.put('/user/{user_id}/{username}/{age}')
async def update_users(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')], username: Annotated[str, Path(min_length=5, max_length=50, description='Enter username', example='UrbanUser')], age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    try:
        edit_user = users[user_id - 1]
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')

@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]):
    num = len(users)
    for i, user in enumerate(users):
        if user.id == user_id:
            num = i
    if num == len(users):
        raise HTTPException(status_code=404, detail='User was not found')
    users.pop(num)
    return users

