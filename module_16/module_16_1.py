from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Главная страница'}

@app.get('/user/admin')
async def admin():
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def users(user_id: int):
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get('/user')
async def user_info(username: str = 'User', age: int = 18):
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}
