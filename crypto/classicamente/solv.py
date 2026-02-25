enc = "f{anuiraaso_lfltnfi_sin_aime_rotpze_gne_ca_roi}_"

length = len(enc)//4
block = [enc[length*i:length*(i+1)] for i in range(4)]

flag = ""
for i in range(length):
    flag += "".join(col[i] for col in block)

print(flag)
