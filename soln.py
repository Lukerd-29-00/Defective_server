from pwn import *
import random
import json
import subprocess

CHALLENGES = [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0]

HOST = 'localhost'
PORT = 3000

r = remote(HOST,PORT)

with open("public_key.json",'r') as f:
    key = json.loads(f.read())

e = key['e']
N = key['N']
ssq = key['s^e']

for challenge in CHALLENGES:
    rand = random.randint(0,N-1)
    if challenge == 0:
        initial = (pow(rand,e,N) * pow(ssq,-1,N)) % N
    else:
        initial = pow(rand,e,N)
    r.sendline(str(initial).encode('utf-8'))
    r.recvline()
    r.sendline(str(rand).encode('utf-8'))

r.interactive()

        

