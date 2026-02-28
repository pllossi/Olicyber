#!/usr/bin/env python3

flag = 'fcnpb}l3_o8fa_tse2g4r4d1{g4n_10n1s77'

def encrypt(flag):
    rows = [flag[i:i+6] for i in range(0, len(flag),6)]
    print(rows)
    res = ""
    for i in range(len(rows)):
        print("i "+ str(i))
        for j in range(len(rows)):
            print("j " + str(j))
            res += rows[j][(i+j) % len(rows[0])]
            print(rows[j][(i+j) % len(rows[0])])
            print("att res: " + res)
    return res

print(encrypt(flag))


