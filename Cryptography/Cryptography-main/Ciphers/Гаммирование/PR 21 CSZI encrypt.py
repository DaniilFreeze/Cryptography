# Шифрование

a = [chr(i) for i in range(ord('а'), ord('я')+1)]
print(a)

# Генератор псевдослучайных чисел

A = int(input("Введите параметр А: "))
C = int(input("Введите параметр C: "))
T_0 = int(input("Введите параметр T(0): "))
b = 5
M = pow(2, b)
word = input("Введите Ваше слово: ")

psevdo_spisok = []

by = []

for i in word:
    by.append(a.index(i))

print("Список номеров букв русского алфавита:\n ", by)

bit_word = [format(x, 'b') for x in by]
print("Бинарный список номеров букв русского алфавита:\n", bit_word)

print("Процесс генерации псевдослучайных чисел: ")
for i in range(1, len(word)+1):
    if i == 1:
        psevdo_spisok.append(((A * T_0) + C)%M)
        print(f"T_{i} = ", format(psevdo_spisok[i-1], 'b'))

    else:
        psevdo_spisok.append(((A * psevdo_spisok[i-2]) + C)%M)
        print(f"T_{i} = ", format(psevdo_spisok[i-1], 'b'))
        
print("Список псевдослучайных чисел:\n ", psevdo_spisok)

output = []
for j in range(len(psevdo_spisok)):
    output.append(format(psevdo_spisok[j], 'b'))

print("Список псевдослучайных чисел в бинарном виде:\n ", output)

summa_shifr = []
for g in range(len(word)):
    summa_shifr.append(format(int(bit_word[g], 2) + int(output[g], 2), 'b'))

summa_shifr = [int(i, 2) for i in summa_shifr]
print("Итоговый зашифрованный текст в числовом виде:\n ", summa_shifr)
c = []
for q in summa_shifr:
    c.append(a[q%32])
    
print("Зашифрованный текст: ", *c, sep='')

