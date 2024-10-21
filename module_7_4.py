"""Задание:
Создайте новый проект или продолжите работу в текущем проекте.
Напишите код, который форматирует строки для следующих сценариев.
Укажите переменные, которые должны быть вставлены в каждую строку"""


#Пример входных данных
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

#Использование %:
formatted_team1_num = "В команде Мастера кода участников: %s !" % team1_num
print(formatted_team1_num)
formatted_teams_num = "Итого сегодня в командах участников: %s и %d !" % (team1_num, team2_num)
print(formatted_teams_num)
# Форматирование с использованием format()
formatted_score_2 = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(formatted_score_2)
formatted_team2_time = "Волшебники данных решили задачи за {} ".format(team2_time)
print(formatted_team2_time)
# Форматирование с использованием f-строк
formatted_scores = f"Команды решили {score_1} и {score_2} задач."
print(formatted_scores)
# 6. Исход соревнования
if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

formatted_challenge_result = f"Результат битвы: {challenge_result}"
print(formatted_challenge_result)
# 7. Количество задач и среднее время решения
formatted_tasks_info = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."
print(formatted_tasks_info)