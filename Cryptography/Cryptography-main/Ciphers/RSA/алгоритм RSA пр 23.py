import math
# алфавит
alf = [chr(i) for i in range(ord('а'), ord('я')+1)]

# шаг 1 (подбор взаимно простых чисел)
p = int(input('Введите параметр p (подсказка: простое число): '))
q = int(input('Введите параметр q (подсказка: простое число): '))
 
# шаг 2 (вычисление значения n)
n = p*q
print("n =", n)
 
# шаг 3 (вычисление значения phi)
phi = (p-1)*(q-1)
 
# шаг 4 (ввод параметра e)
e = int(input('Введите параметр e, но будьте осторожны,\n'
f'для правильной работы необходимо,\nчтобы e было взаимно простым с результатом phi = {phi} : '))

print("e =", e)
# шаг 5 (расчет d)
d = 2
while(math.fmod(d*e, phi)):
    if (math.fmod(d*e, phi) == 1):
        break
    else:
        d += 1
print("d =", d)

print(f'Открытый ключ: {e, n}')
print(f'Закрытый ключ: {d, n}')
 
# составление исходного текста
msg = input('Введите исxодное послание: ')
print(f'Исходное послание: {msg}')
 
# процесс шифрования
C = ''
spisok = []
for i in msg:
    C += alf[(pow(alf.index(i), e)%n)%len(alf)]
    spisok.append(pow(alf.index(i), e)%n)
print(f'Зашифрованное послание: {C}')
print('Позиции символов шифрованного текста: ', spisok)

# процесс дешифрования
M = ''
for j in spisok:
    M += alf[(pow(j, d)%n)%len(alf)]
print(f'Расшифрованный текст: {M}')
