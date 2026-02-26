from pwn import remote

r = remote("market.challs.olicyber.it", 10005)

r.reciveuntil(b"cosa vuoi comprare?\n>")
r.sendline(b"")