
# В свободное время Вася любит играть в компьютерные игры. Однажды у него появилась классная идея для сюжета игры. Чтобы воплотить её в жизнь, он начал изучать геймдизайн. 
#Создавать игру он начал с главного героя и его системы прокачки.

# Напишите программу, которая определяет уровень персонажа в компьютерной игре. Пользователь вводит число «очков опыта», а программа вычисляет уровень. 
#Новый уровень даётся при достижении 1000, 2500 и 5000 «очков опыта». Начальный уровень равен единице.

score_user = int(input('Введите количество опыта: '))
level_user = 4
if score_user < 1000:
    level_user = 1
elif score_user < 2500:
    level_user = 2
elif score_user < 5000:
    level_user = 3
print('Ваш уровень:' , level_user)