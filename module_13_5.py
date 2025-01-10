import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import API_TOKEN


 # Замените на ваш токен

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Создание клавиатуры
kb = ReplyKeyboardMarkup(resize_keyboard=True)
butt_info = KeyboardButton('Информация')
butt_exit = KeyboardButton('Выход')
kb.add(butt_info).add(butt_exit)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет', reply_markup=kb)

@dp.message_handler(text='Информация')
async def info(message: types.Message):
    await message.answer('Информация', reply_markup=kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)