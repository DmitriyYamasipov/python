gradus_out = int(input('Сколько градусов: '))
gogo = 0
while gradus_out >= 15:
    gogo += 20
    gradus_out -= 2
    if gradus_out <= 15:
        break
    gogo += 10
print(gogo)
print('Забег окончен')