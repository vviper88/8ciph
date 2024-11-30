#!/usr/bin/env python3

otp_file = input("File to read OTP from? ")
message_to_decode = input("Message to decode? ")
message_to_dec_list = message_to_decode.split("  ")

with open(otp_file, "r") as file:
    file_lines = file.readlines()
    file_lines.pop(0)
    file_lines.pop(-1)
    file.close()

for number in message_to_dec_list:
    for line in file_lines:
        if number in line:
            if list(line)[1] == "L":
                print(last_character, end="")
            else:
                print(list(line)[0], end="")
                last_character = list(line)[0]
print("")