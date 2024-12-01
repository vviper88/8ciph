#!/usr/bin/env python3
import base64
import secrets

otp_file = input("File to read OTP from? ")
message_to_encode = input("Message to encode? ")

with open(otp_file, "r") as file:
    file_lines = file.readlines()
    file_lines.pop(0)
    file_lines.pop(-1)
    file.close()
print(f"Base64 to be encrypted: {base64.b64encode(message_to_encode.encode()).decode()}")
message_list = list(base64.b64encode(message_to_encode.encode()).decode())
character_last = ""
for character in message_list:
    if character_last == character:
        for line in file_lines:
            if "L" == list(line)[1]:
                print(line.split()[1], " ", end="")
    else:
        for line in file_lines:
            if character == list(line)[0]:
                print(line.split()[secrets.randbelow(3) + 1], " ", end="")
                break
    character_last = character
print('')
