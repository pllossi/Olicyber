from Crypto.Cipher import *
from Crypto.Util.Padding import *
from pwn import remote

r = remote("crypto-07.challs.olicyber.it",30000)