rusk = int(input('Введите количество баллов по русскому языку: '))
matematika = int(input('Введите количество баллов по математике: '))
informatik = int(input('Введите количество баллов по информатике: '))
score = 270
score_exams = rusk + matematika + informatik

if score_exams >= score:
  print('Поздравляю, ты поступил на бюджет!')
else:
  print('К сожалению, ты не прошёл на бюджет.')