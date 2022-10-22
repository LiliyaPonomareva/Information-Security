import binascii

def ciphertext(text, key):
    encoded_bytes = text.encode('utf-8', 'replace')
    x = binascii.hexlify(encoded_bytes)
    y = str(x, 'utf-8')
    binary = lambda x: " ".join(reversed(
        [i + j for i, j in zip(*[["{0:04b}".format(int(c, 16)) for c in reversed("0" + x)][n::2] for n in [1, 0]])]))
    x1 = binary(y)

    key1 = bytearray.fromhex(key)
    x_key = binascii.hexlify(key1)
    y_key = str(x_key, 'utf-8')
    x1_key = binary(y_key)

    text2 = ""
    for i in range(len(x1)):
        if x1[i] == ' ':
            text2 += ' '
        elif x1[i] == x1_key[i]:
            text2 += '0'
        elif x1[i] != x1_key[i]:
            text2 += '1'

    text2_ = text2.split()
    crypt = ' '
    for n in text2_:
        crypt += hex(int(n, 2))[2:] + ' '
    return crypt

def getkey(cipher, text):
    encoded_bytes = bytearray.fromhex(cipher)
    x = binascii.hexlify(encoded_bytes)
    y = str(x, 'utf-8')
    binary = lambda x: " ".join(reversed(
        [i + j for i, j in zip(*[["{0:04b}".format(int(c, 16)) for c in reversed("0" + x)][n::2] for n in [1, 0]])]))
    x1 = binary(y)

    text1 = text.encode('utf-8', 'replace')
    x_text = binascii.hexlify(text1)
    y_text = str(x_text, 'utf-8')
    x1_text = binary(y_text)

    key = ""
    for i in range(len(x1)):
        if x1[i] == ' ':
            key += ' '
        elif x1[i] == x1_text[i]:
            key += '0'
        elif x1[i] != x1_text[i]:
            key += '1'

    key_ = key.split()
    pos_key = ' '
    for n in key_:
        pos_key += hex(int(n, 2))[2:] + ' '
    return pos_key

a = 'Штирлиц – Вы Герой!!!'
key = "05 0C 17 7F 0E 4E 37 D2 94 10 09 2E 22 57 FF C8 0B B2 70 54 05 0C 17 7F 0E 4E 37 D2 94 10 09 2E 22 57 FF C8 05"
text = "С Новым Годом, друзья"

cipher = ciphertext(a, key)
print("Шифротекст:", cipher)
print("Ключ:", getkey(cipher, a))

