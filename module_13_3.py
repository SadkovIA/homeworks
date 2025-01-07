import asyncio


from aiogram import types, Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage



API_TOKEN = ''  # Укажите ваш токен бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def all_start_user(message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler(text='Привет')
async def urban_message(message):
    print('мы получили новое сообщение')

@dp.message_handler()
async def all_message_user(message):
    print('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
