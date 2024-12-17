"""Цель: приобрести навык использования
асинхронного запуска функций на практике

Задача "Асинхронные силачи":"""

import asyncio


async def start_strongman(name:str, power:int): # асинхронная функция
    print(f"Силач {name} с силой {power} начал работу")
    for i in range(1, 6):
        await asyncio.sleep(1 / power)  # Задержка обратно пропорциональная силе
        print(f'Силач {name} поднял {i} шар')

    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    # Создаем таски для трех силачей с разными именами и силой
    tasks = [
        start_strongman('Pasha', 3),
        start_strongman('Denis', 4),
        start_strongman('Apollon', 5)
    ]

    # Ожидаем завершения всех tasks
    await asyncio.gather(*tasks)
    """Функция gather() модуля asyncio одновременно запускает объекты awaitable,
     переданные в функцию как последовательность *aws.
Функция asyncio.gather() представляет то же объект ожидания awaitable
 и запускается оператором await."""


# Запускаем асинхронную функцию start_tournament
if __name__ == "__main__":
    asyncio.run(start_tournament())



