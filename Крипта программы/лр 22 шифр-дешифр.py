rounds = int(input('Введите кол-во раундов: '))
key = input('Введите ключ для шифрования: ')
text = input('Введите текст, который необходимо зашифровать: ')
blocks = [] 
if len(text) % 2 != 0:
    text += ' '

for i in range(0, len(text), 2):
    blocks.append(text[i:i + 2])

L = ord(blocks[0][0])
R = ord(blocks[0][1])
key_pos = 0
def feistel(L,R, key_pos):
    for i in range(rounds):
        K = ord(key[key_pos % len(key)::][0])
        temp = R ^ (L ^ K)
        R = L
        L = temp
        key_pos += 1 
        end = (chr(R) + chr(L))
    return end, key_pos

shifr = []
for x in blocks:
    blocks, key_pos = feistel(ord(x[0]), ord(x[1]), key_pos)
    shifr.append(blocks)

print(f"Зашифрованное сообщение: {''.join(shifr)}")

def feistel_dec(L,R, key_pos):
    for i in range(rounds):
        K = ord(key[key_pos % len(key)::][0])
        temp = R ^ (L ^ K)
        R = L
        L = temp
        key_pos -= 1 
        end = (chr(R) + chr(L))
    return end, key_pos
   
deshifr = []
key_pos -= 1
for x in shifr[::-1]:
    blocks, key_pos = feistel_dec(ord(x[0]), ord(x[1]), key_pos)
    deshifr.append(blocks)
deshifr_text = ''
for i in deshifr[::-1]:
    deshifr_text += i
print("Дешифрованное сообщение: ", deshifr_text)
