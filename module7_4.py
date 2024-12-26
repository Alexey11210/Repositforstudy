team1_num = 5
print('В команде Мастера кода участников: %s' % '5')
team2_num = 6
print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s' % {'team1_num': 5, 'team2_num': 6})
score_2 = 42
score_1 = 40
print('Команда Волшебники данных решила задач: {}'.format(score_2))
team1_time = 18015.2
team2_time = team1_time/score_1*score_2
print('Волшебники данных решили задачи за {} с !'.format(team1_time))
print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'
print(f'Результат битвы: {challenge_result}!')

tasks_total = score_1 + score_2
time_avg = 18015.2/40
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
