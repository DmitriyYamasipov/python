#score_students = int(input('Введите балл:  '))
#medal = int(input('Золотая медаль "1"-есть, "0"-нету  '))
#score_ideal = 280
#if score_students > score_ideal and medal == 1:
#    print('Поздравляем! Ты поступил!')
#else:
#    print('К сожалению, ты не прошёл в наш университет.')

t_microb = int(input('Введите темепературу микробов:  '))
t_min = 0
t_max = 100
if t_microb < t_min or t_microb > t_max:
    print('Опасность !!!')
else:
    print('Всё в норме.')
