from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def all_users():
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=5, max_length=50, description='Enter username', example='UrbanUser')], age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return {'message': f'User {user_id} is registered'}

@app.put('/user/{user_id}/{username}/{age}')
async def update_users(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')], username: Annotated[str, Path(min_length=5, max_length=50, description='Enter username', example='UrbanUser')], age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return {'message': f'The user {user_id} is updated'}

@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]):
    del users[f'{user_id}']
    return {'message': f'User {user_id} has been deleted.'}
