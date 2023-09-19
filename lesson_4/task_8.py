print('Задача 8. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно 

number_1 = int(input('Введите перове число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))
number_max = number_1

if number_max < number_2:
  number_max = number_2

if number_max < number_3:
  number_max = number_3

print(number_max)