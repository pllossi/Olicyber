from pwn import remote
import os
import base64


shulf_hex = input("hex: \n")
shulf_bytes = bytes.fromhex(shulf_hex)


payload = os.urandom(500)
exp_b85 = base64.b85encode(payload)

print("Hex message:")
print(payload.hex())



enc_payload_hex =  input("B85: \n")
enc_payload =  bytes.fromhex(enc_payload_hex)

mappa_inversa = {}
for i in range(len(enc_payload)):
    mappa_inversa[i]= exp_b85[i]

flag_b85 = bytearray()
for char in shulf_bytes:
    flag_b85.append(mappa_inversa[char])

flag = base64.b85decode(flag_b85)
print(flag.decode(encoding='latin-1',errors="false"))
