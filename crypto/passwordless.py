sendin= "Am" + "a"*16 + "ministratore"
print(sendin)
token = bytes.fromhex("dc9a9174a06faf1deae74f0062250aaede39046d6ac0a72b79e7952e06ce6bb47f4e3060e6ac4664ef6f1c2c7de699f300c1aa6a161f582cbccf8563bef5b1bfbeb32be6c7ce6c799a02daa54d40604fc7e8099423da78b60246d3c8251ef7eb")
new_token= token[:16]+token[32:]
print(new_token.hex())