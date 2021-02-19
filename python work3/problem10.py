
#1. write a variable with number
num = 100

#2. Is this number a three digit number?
"""num1=int(input("Enter your number:"))"""
if(num < 1000 and num > 99):
    print("It's a 3 digit number")
else:
    print("is not a 3 digit number")

#3. Is it EVEN or ODD number?
if (num // 2) != 0:
    print("100 in an EVEN number")
else:
    print("100 is an ODD number")

#4 Can 100 be divided by 31 without remainder
if (num % 17) != 0 or (num > 150) and (num == 13**2):
    print("Show the number")