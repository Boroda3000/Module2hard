import random
j = []
for i in range(3, 21):
    j += [i]
n = random.choice(j)
print('Выбранное число: ', n)
password = 'Пароль: '
for a in range(1, n):
    for b in range(a + 1, n):
        if n % (a + b) == 0:
            password += str(a) + str(b)
        else:
            continue
print(password)