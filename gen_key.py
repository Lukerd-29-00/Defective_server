from Crypto.Util import number
import json
import random

N = number.getPrime(1024) * number.getPrime(1024)

s = random.SystemRandom().randint(0,N-1)
e = 65536
s_to_e = pow(s,e,N)

with open("public_key.json",'w') as f:
    f.write(json.dumps({
        "s^e": s_to_e,
        "N": N,
        "e": e
}))

with open("private_key.json",'w') as f:
    f.write(json.dumps({
        "s": s
    }))