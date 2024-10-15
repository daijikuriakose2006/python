"""
Author: daiji Kuriakose
Date:10-10-2024
Title:Python program to check weather the given number is positive or not
"""
number=int(input("Enter a number"))
if number>0:
    print("The given number:",number,"is positive")
elif number<0:
    print("The given number",number,"is negative")
else:
    print("the given number",number,"is Zero")