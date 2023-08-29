ishod_alf = [chr(i) for i in range(ord('A'), ord('Z')+1)]
ishod_alf.extend([' ', '.', ',', '!', ':', ';', '?', '-'])
print(ishod_alf)
shifr_alf = []
shifr_alf.extend([i for i in ishod_alf[21::]])
shifr_alf.extend([i for i in ishod_alf[10:21]])
shifr_alf.extend([i for i in ishod_alf[0:10]])
print(shifr_alf)

shifr_text = input('Введите наглое послание царя Леонида, которое нужно расшифровать, милорд: ')
k = int(input('Введите примененное смещение (ключ), милорд: '))
n = len(ishod_alf)
ishod_text = ''
for q in shifr_text:
    i = ((shifr_alf.index(q) + n) - k)%n
    ishod_text += ishod_alf[i]
print(ishod_text)
