"""author: Daiji Kuriakose
   Date  : 30/11/2024
   Write a Python program to check weather the mobile number is valid or not:"""
def mobile_number():
    number=input("Enter number")
    if len(number)==10 and number[0] in '789':
        print("The mobile number is valid")
    else:
        print("The number is not valid")
mobile_number()
