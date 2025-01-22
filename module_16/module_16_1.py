from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return 'Главная страница'

@app.get('/user/admin')
async def admin():
    return 'Вы вошли как администратор'

@app.get('/user/{user_id}')
async def users(user_id: int):
    return f'Вы вошли как пользователь № {user_id}'

@app.get('/user')
async def user_info(username: str = 'User', age: int = 18):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
