from pwn import remote
import string


r = remote("test.challs.olicyber.it", 15004)
r.recvuntil(b"in quanto con una sola mossa (il secondo pulsante) tutti i contatori segnano 5.")
resp = []
r.recvline()
livello = r.recvline()
while True:

    vals = r.recvline().decode()
    nums = vals.strip().split(" ")
    nums = [int(nums[i]) for i in range(len(nums))]
    print(nums)
    buttons = []
    line = r.recvline().decode().strip()
    while line != "":ww
        buttons.append(line.split())
        line = r.recvline().decode().strip()
    
    print(buttons)

    for i,button in enumerate(buttons):
        cont0 = button[0]
        print(cont0)
        cont_index=string.ascii_uppercase.index(cont0)
        cont_val =  nums[cont_index]
        ripet = 5 - cont_val
        resp += [str(i+1)]*ripet
        
    
    print(resp)

    response= ' '.join(resp)
    r.sendline(response.encode())
    resp = []
    r.recvuntil(b"Ottimo!\n")
    r.recvline()
    livello = r.recvline()
    if (not livello.startswith(b"Livello")):
        print(livello)
        break

r.interactive()