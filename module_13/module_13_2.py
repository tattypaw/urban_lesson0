from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

from aiogram.utils.executor import start_polling

api = '7356849063:AAHmC4m8ZAvjYWRT4vO4Blw75PrJVHjcUd0'
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands = ['start'])
async def start(message):
    print('Привет! Я бот, помогающий твоему здоровью.')

@dp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)