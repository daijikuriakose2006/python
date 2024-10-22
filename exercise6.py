"""author: Daiji Kuriakose
   Date  : 22/10/2024
   Write a Python program to find largest of three numbers:"""
first_number=int(input("enter first number"))
second_number=int(input("enter second number"))
third_number=int(input("enter third number"))
if (first_number>second_number)and(first_number>third_number):
    print("The largest number is",first_number)
elif (second_number>first_number)and(second_number>third_number):
    print("The largest number is",second_number)
elif (third_number>first_number)and(third_number>second_number):
    print("The largest number is",third_number)
else:
    print("three numbers are equal")