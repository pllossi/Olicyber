from pwn import *
import base64

def findEncoding(name):
    if "base64!" in name :
        return "base64"
    elif "esadecimale!"in name:
        return "hex"
    elif "binario!" in name:
        return "bin"
    


def decodeWay(way):
    if("da" in way):
        return "da"
    else:
        return "a"
    
def decode(data, encoding):
    if encoding == "base64":
        return base64.b64decode(data).decode()
    elif encoding == "hex":
        return bytes.fromhex().decode()
    elif encoding == "bin":
        n = int(data, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    
def encode(data,encoding):
    if(encoding == "base64"):
        return base64.b64encode(data.encode()).decode()
    elif(encoding == "hex"):
        return data.hex()
    elif(encoding == "bin"):
        return ''.join(format(ord(i), '08b') for i in data)

while True:
    r= remote("based.challs.olicyber.it", 10600)
    r.recvuntil(b"Converti questo ")
    enc= r.recvline().decode()
    way = decodeWay(enc)
    encoding = findEncoding(enc)
    r.recvuntil(b": ")
    data = r.recvline().decode().strip().replace("}","")
    if way == "da":
        result = decode(data, encoding)
    else:
        result = encode(data, encoding)
    print(way)
    print(data)
    print(encoding)
    print(result)
    resoultprint= '{"answer": "' + result + '"}'
    print(resoultprint)
    r.sendline(resoultprint)

r.interactive()
