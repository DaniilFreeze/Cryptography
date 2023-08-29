# Дешифрование

a = [chr(i) for i in range(ord('а'), ord('я')+1)]
print(a)

# Генератор псевдослучайных чисел

A = int(input("Прошу, Введите параметр А: "))
C = int(input("Прошу, Введите параметр C: "))
T_0 = int(input("Прошу, Введите параметр T(0): "))
b = 5
M = pow(2, b)
text = input("Введите текст, который необходимо расшифровать, милорд: ")

psevdo_spisok = []

by = []

for i in text:
    by.append(a.index(i)+32)

print("Специально для Вас и Вашего удобства представлен список номеров букв русского алфавита, прошу:\n ", by)

bit_word = [format(x, 'b') for x in by]
print("Позвольте, бинарный список номеров букв русского алфавита, милорд:\n", bit_word)

print("Вы можете наблюдать на данном этапе процесс генерации псевдослучайных чисел, о, милорд: ")
for i in range(1, len(text)+1):
    if i == 1:
        psevdo_spisok.append(((A * T_0) + C)%M)
        print(f"T_{i} = ", format(psevdo_spisok[i-1], 'b'))

    else:
        psevdo_spisok.append(((A * psevdo_spisok[i-2]) + C)%M)
        print(f"T_{i} = ", format(psevdo_spisok[i-1], 'b'))
        
print("Милорд, вот список псевдослучайных чисел, клянусь:\n ", psevdo_spisok)

output = []
for j in range(len(psevdo_spisok)):
    output.append(format(psevdo_spisok[j], 'b'))

print("Милорд, а вот это уже список псевдослучайных чисел в бинарном виде:\n ", output)

summa_shifr = []
for g in range(len(text)):
    summa_shifr.append(format(int(bit_word[g], 2) - int(output[g], 2), 'b'))

print(summa_shifr)
summa_shifr = [int(i, 2) for i in summa_shifr]
print("Ничего нетривиального, милорд, лишь итоговый дешифрованный текст в числовом виде:\n ", summa_shifr)
c = []
for q in summa_shifr:
    c.append(a[q%32])
    
print("Дешифрованный текст: ", *c, sep='')
