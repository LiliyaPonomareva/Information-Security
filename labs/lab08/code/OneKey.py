import string
import random


def key_gen(text):
    key = ' '.join(random.choice(string.hexdigits)+random.choice(string.hexdigits) for _ in range(len(text)))
    return key


P1 = 'НаВашисходящийот1204'
P2 = 'ВСеверныйфилиалБанка'
key = key_gen(P1)
print("Ключ:", key)


def crypt(text1, text2):
    key1 = [ord(i) for i in key]
    text1 = [ord(i) for i in text1]
    text2 = [ord(i) for i in text2]
    crypt1 = ''.join(chr(a ^ b) for a, b in zip(text1, key1))
    crypt2 = ''.join(chr(a ^ b) for a, b in zip(text2, key1))
    return crypt1, crypt2


code1, code2 = crypt(P1, P2)
print("Шифротекст 1:", code1)
print("Шифротекст 2:", code2)


def decrypt(code1, code2):
    code1 = [ord(i) for i in code1]
    code2 = [ord(i) for i in code2]
    key_ = ''.join(chr(a ^ b) for a, b in zip(code1, code2))
    text1 = ''.join(chr(a ^ b) for a, b in zip(code1, key_))
    text2 = ''.join(chr(a ^ b) for a, b in zip(code1, key_))
    return text1, text2


txt1, txt2 = crypt(code1, code2)
print("Дешифровка 1 текста:", txt1)
print("Дешифровка 2 текста:", txt2)

