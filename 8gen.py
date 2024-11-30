#!/usr/bin/env python3
import secrets

min_num = 10000000
max_num = 99999999
LBL_CHARS = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!?.,:][/&%@`'~+-_ ")
used_crypts = []

print("-- BEGIN PAD --")
for i in LBL_CHARS:
    while True:
        ciph = str(secrets.randbelow(max_num - min_num + 1) + min_num)
        if ciph not in used_crypts and "666" not in ciph:
            break
    print(f"{i}: {ciph}")
while True:
    ciph = str(secrets.randbelow(max_num - min_num + 1) + min_num)
    if ciph not in used_crypts and "666" not in ciph:
        break
print(f"RLL: {ciph}")
print("-- END PAD --")