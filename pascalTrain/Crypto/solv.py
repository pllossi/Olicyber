flag = 'flag{redacted_redacted_redacted_ABC}'
 
def encrypt(flag):
    rows = [flag[i:i+6] for i in range(0, len(flag),6)]
    for r in rows:
        print(r)
    print()
    print()
    res = ""
    for i in range(len(rows)):
        for j in range(len(rows)):
            res += rows[j][(i+j) % len(rows[0])]
    rows = [res[i:i+6] for i in range(0,len(res),6)]
    for r in rows:
        print(r)
    return res

def decript(cipertext):
    lungBlocchi=6
    nBlocchi= len(cipertext)//lungBlocchi
    sol=['']*len(cipertext)
    n = 0
    for i in range(nBlocchi):
        for j in range(nBlocchi):
                pos_orig = j * lungBlocchi +(i+j)%lungBlocchi
                sol[pos_orig] =cipertext[n]
                n+=1
    return "".join(sol)

 
print(encrypt(flag)) 
encr="fhuth}lo__atapdus_geiden{_yn_iI_o'cg"
print(decript(encr))