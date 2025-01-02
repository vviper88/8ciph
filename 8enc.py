#!/usr/bin/env python3
import base64
import secrets
import sys
otp_file = sys.argv[1]
message_to_encode = sys.argv[2]

with open(otp_file, "r") as file:
    file_lines = file.readlines()
    file_lines.pop(0)
    file_lines.pop(-1)
    file.close()
print(f"Base64 to be encrypted: {base64.b64encode(message_to_encode.encode()).decode()}")
message_list = list(base64.b64encode(message_to_encode.encode()).decode())
character_last = ""
if secrets.randbelow(5) == 1:
    print((secrets.randbelow(99999999 - 10000000  + 1) + 10000000), " ", end="")
for character in message_list:
    if character_last == character:
        for line in file_lines:
            if "L" == list(line)[1]:
                print(line.split()[secrets.randbelow(3) + 1], " ", end="")
    else:
        for line in file_lines:
            if character == list(line)[0]:
                print(line.split()[secrets.randbelow(3) + 1], " ", end="")
                break
    if secrets.randbelow(5) == 1:
        print((secrets.randbelow(99999999 - 10000000  + 1) + 10000000), " ", end="")
    character_last = character
print('')
