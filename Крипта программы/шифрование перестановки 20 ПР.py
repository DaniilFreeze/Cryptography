ishod_alf = [chr(i) for i in range(ord('A'), ord('Z')+1)]
ishod_alf.extend([' ', '.', ',', '!', ':', ';', '?', '-'])
print(ishod_alf)
shifr_alf = []
shifr_alf.extend([i for i in ishod_alf[21::]])
shifr_alf.extend([i for i in ishod_alf[10:21]])
shifr_alf.extend([i for i in ishod_alf[0:10]])
print(shifr_alf)

text = input('Введите Ваше послание, милорд: ')
k = int(input('Введите желаемое смещение (ключ), милорд: '))
n = len(ishod_alf)
shif = ''
for q in text:
    i = (ishod_alf.index(q)+k)%n
    shif += shifr_alf[i]
print(shif)
