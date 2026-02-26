from pwn import *
exe = ELF("./Software/pwntools3/sw-19")

r = remote("software-19.challs.olicyber.it", 13002)


r.recvuntil(b"... Invia un qualsiasi carattere per iniziare ...")
r.send(b"a")
for i in range(20):
    r.recvuntil(b"->")
    richiest = r.recvuntil(b":")
    richiest = richiest[1:-1]
    ind = exe.sym[richiest]
    ind = hex(ind)
    r.sendline(ind)
r.interactive()
        
    