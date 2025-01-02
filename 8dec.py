#!/usr/bin/env python3
import base64
import sys 
otp_file = sys.argv[1]
message_to_decode = sys.argv[2]
message_to_dec_list = message_to_decode.split("  ")
message_near_end_list = []
with open(otp_file, "r") as file:
    file_lines = file.readlines()
    file_lines.pop(0)
    file_lines.pop(-1)
    file.close()

for number in message_to_dec_list:
    for line in file_lines:
        if number in line:
            if list(line)[1] == "L":
                message_near_end_list.append(last_character)
            else:
                message_near_end_list.append(list(line)[0])
                last_character = list(line)[0]
print(f"Base64 to be decoded: {''.join(message_near_end_list)}")
print(base64.b64decode("".join(message_near_end_list)).decode())
