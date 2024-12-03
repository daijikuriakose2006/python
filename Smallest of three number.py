"""
Author: daiji Kuriakose
Date:15-10-2024
Title:Python program to determine the smallest of three number
"""
number1=int(input("Enter first number"))
number2=int(input("Enter second number"))
number3=int(input("Enter third number"))
if (number1<number2)and(number1<number3):
    print("first number",number1,"is smaller")
elif (number2<number1)and(number2<number3):
    print("second number",number2,"is smaller")
elif (number3<number1)and(number3<number2):
    print("third number",number3,"is smaller")
else:
    print("three numbers are equal")
