"""
Author: daiji Kuriakose
Date:15-10-2024
Title:Python program to find simple interest
"""
amount=int(input("Enter the amount"))
years=float(input("Enter the number of years"))
rate=float(input("Enter the interest rate"))
si=(amount*years*rate)/100
print("simple interest=",si)
