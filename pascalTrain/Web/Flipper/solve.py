from base64 import b64encode, b64decode

def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])


token = "g9f+kZun+a4OTqsWkW5nAJ/LCcS10gstxN2Z8xM7zGk="
token_decod= b64decode(token)
user = token_decod[:16]
punti = token_decod[16:]

plain=b";pts=00000000000"
puntifin = b";pts=10000000000"

b1= xor(user,plain)

b2= xor(b1,puntifin)

NuovoToken=b2+punti
NuovoToken = b64encode(NuovoToken)
print(NuovoToken)

