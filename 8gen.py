#!/usr/bin/env python3
import secrets

min_num = 10000000
max_num = 99999999
LBL_CHARS = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=")
used_crypts = []

print("-- BEGIN PAD --")
for i in LBL_CHARS:
    while True:
        ciph = str(secrets.randbelow(max_num - min_num + 1) + min_num)
        if ciph not in used_crypts and "666" not in ciph:
            used_crypts.append(ciph)
            ciph2 = str(secrets.randbelow(max_num - min_num + 1) + min_num)
            if ciph2 not in used_crypts and "666" not in ciph2:
                used_crypts.append(ciph2)
                ciph3 = str(secrets.randbelow(max_num - min_num + 1) + min_num)
                if ciph3 not in used_crypts and "666" not in ciph3:
                    used_crypts.append(ciph3)
                    break
    print(f"{i}: {ciph} {ciph2} {ciph3}")
while True:
    ciph = str(secrets.randbelow(max_num - min_num + 1) + min_num)
    if ciph not in used_crypts and "666" not in ciph:
        used_crypts.append(ciph)
        ciph2 = str(secrets.randbelow(max_num - min_num + 1) + min_num)
        if ciph2 not in used_crypts and "666" not in ciph2:
            used_crypts.append(ciph2)
            ciph3 = str(secrets.randbelow(max_num - min_num + 1) + min_num)
            if ciph3 not in used_crypts and "666" not in ciph3:
                used_crypts.append(ciph3)
                break
print(f"RLL: {ciph} {ciph2} {ciph3}")
print("-- END PAD --")
