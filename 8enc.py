#!/usr/bin/env python3

otp_file = input("File to read OTP from? ")
message_to_encode = input("Message to encode? ")

with open(otp_file, "r") as file:
    file_lines = file.readlines()
    file_lines.pop(0)
    file_lines.pop(-1)
    file.close()

message_list = list(message_to_encode)
character_last = ""
for character in message_list:
    if character_last == character:
        for line in file_lines:
            if "L" == list(line)[1]:
                print(line.split()[1], " ", end="")
    else:
        for line in file_lines:
            if character == list(line)[0]:
                print(line.split()[1], " ", end="")
                break
    character_last = character
print('')
