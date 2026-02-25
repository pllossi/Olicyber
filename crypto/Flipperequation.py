from base64 import b64encode, b64decode

def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])


token = "lE6OTSxu5xm1EbytDdYsM/E/M5eD+rZnP0upzpXSvaU="
token_decod= b64decode(token)
c0 = token_decod[:16]
c1 = token_decod[16:]

plain=b";pts=00000000000"
m1 = b";pts=10000000000"

cAra= xor(c0,plain)

c0New= xor(cAra,m1)

tokennuov=c0New+c1
tokennuov = b64encode(tokennuov)
print(tokennuov)

