import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from config import API_TOKEN


# Создаем экземпляры бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Определяем классы состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Функция для обработки команды "Calories"
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Введите 'Calories' для начала.")

@dp.message_handler(lambda message: message.text.lower() == 'calories')
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

# Функция для обработки возраста
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

# Функция для обработки роста
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

# Функция для обработки веса и вычисления нормы калорий
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)

    data = await state.get_data()
    age = int(data.get('age'))
    growth = int(data.get('growth'))
    weight = int(data.get('weight'))

    # Формула Миффлина - Сан Жеора для мужчин
    # BMR = 10 * weight + 6.25 * growth - 5 * age + 5
    # Для женщин: BMR = 10 * weight + 6.25 * growth - 5 * age - 161
    bmr = 10 * weight + 6.25 * growth - 5 * age + 5  # Для мужчин
    calories = bmr  # Это базовая метаболическая норма (BMR)

    await message.answer(
        f"Ваша норма калорий: {calories:.2f} ккал.")

    await state.finish()  # Завершение состояний

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)