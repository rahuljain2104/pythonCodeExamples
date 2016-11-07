# import math
# from decimal import Decimal as D
#
# sum = D(0)
# sum += D("0.1")
#
# secret_number = int(9)
#
# while True :
#
#     try:
#         number = int(input("please guess a number in (1-10): "))
#
#     except ValueError:
#         print("You didn't enter a number")
#
#     except:
#         print "an unknown error occured"
#
#     if number == secret_number:
#         break
#
#
# print("you guessed it correctly")
#



# enter a string to hide in uppercase :
# secret message : 35647890
# Original Message : HIDE

strng = raw_input("Enter a string : ")

secret_string = ""

for i in strng:
    secret_string = secret_string + str(ord(i)-23)

print secret_string


backup_string = ""
i = 0

while i < len(secret_string)-1:
    if (int(secret_string[i]) != 1):
        backup_string = backup_string + chr(int(secret_string[i] + secret_string[i + 1])+23)
        i = i + 2

print "back up string is : " + backup_string
