#import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import API_TOKEN


class Form(StatesGroup):
    age = State()
    weight = State()
    height = State()

# Создание объектов бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Главное меню
@dp.message_handler(commands=['start'])
async def start_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Рассчитать'))
    keyboard.add(types.KeyboardButton('Информация'))
    await message.answer("Выберите опцию:", reply_markup=keyboard)

# Обработка кнопки 'Рассчитать'
@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'))
    keyboard.add(types.InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas'))
    await message.answer("Выберите опцию:", reply_markup=keyboard)

# Обработка кнопки 'Формулы расчёта'
@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer("Формула Миффлина-Сан Жеора: \n\nДля мужчин: \nBMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) + 5\n\nДля женщин: \nBMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) - 161")
    await call.answer()

# Обработка кнопки 'Рассчитать норму калорий'
@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await Form.age.set()
    await call.message.answer("Введите ваш возраст:")

# Обработка ввода возраста
@dp.message_handler(state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await Form.next()  # Переход к следующему состоянию
    await message.answer("Введите ваш вес в килограммах:")

# Обработка ввода веса
@dp.message_handler(state=Form.weight)
async def process_weight(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    await Form.next()  # Переход к следующему состоянию
    await message.answer("Введите ваш рост в сантиметрах:")

# Обработка ввода роста и расчет калорий
@dp.message_handler(state=Form.height)
async def process_height(message: types.Message, state: FSMContext):
    await state.update_data(height=message.text)
    data = await state.get_data()

    age = int(data['age'])
    weight = float(data['weight'])
    height = float(data['height'])

    # Расчет BMR для мужчин
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
    calories = bmr  # Это базовая метаболическая норма (BMR)

    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал.")
    await message.answer("Спасибо за использование бота!))")
    await state.finish()  # Завершение состояний

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
