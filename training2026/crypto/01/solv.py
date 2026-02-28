cipertext= "fcnpb}l3_o8fa_tse2g4r4d1{g4n_10n1s77"

def decript():
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

print(decript())
