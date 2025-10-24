from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

#devo decriptare aes in ecb con padding a 16 e poi rimuovere il padding con attacco Oracle

flag = 'b0945df717a2ddd1314a8f0f93a716af' #parte di flag è qui
newflag = ''
length = 25
char_dict = [chr(i) for i in range(32, 127)]

for i in range(length):
    for j in range(32, 127):
        guess= char_dict[j-32]
        padded = pad(guess,16)
        crypted = AES.new(padded, AES.MODE_ECB)
        if (crypted==flag):
            newflag += chr(j)
            print(newflag)
            break
