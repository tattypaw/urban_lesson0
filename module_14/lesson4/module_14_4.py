from crud_functions import *

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

button1_1 = KeyboardButton(text='Рассчитать')
button2_1 = KeyboardButton(text='Информация')
button3_1 = KeyboardButton(text='Купить')
kb_1 = ReplyKeyboardMarkup(keyboard=[
        [button1_1,
         button2_1],
         [button3_1]
    ], resize_keyboard = True)

button1_2 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button2_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [button1_2,
         button2_2]
    ], resize_keyboard = True
)

products_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Product1", callback_data="product_buying"),
        InlineKeyboardButton(text="Product2", callback_data="product_buying"),
        InlineKeyboardButton(text="Product3", callback_data="product_buying"),
        InlineKeyboardButton(text="Product4", callback_data="product_buying")]
    ]
)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

products = get_all_products()

@dp.message_handler(text = 'Купить')
async def get_buying_list(message):
    i = 1
    for product in products:
        await message.answer(f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}' )
        with open(f'files/{i}.png', "rb") as img:
            await message.answer_photo(img)
        i += 1
    await message.answer('Выберите продукт для покупки:', reply_markup=products_kb)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler(text = 'Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kb_2)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()

@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    await UserState.weight.set()
    calories = 10*int(data['weight'])+6.25*int(data['growth'])-5*int(data['age']) - 161
    await message.answer(f'Ваша норма калорий: {calories}')
    await state.finish()

@dp.message_handler(commands = ['start'])
async def start(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb_1)

@dp.message_handler(text = 'Информация')
async def set_age(message):
    await message.answer('Бот создан для отработки учебных навыков.')

@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)