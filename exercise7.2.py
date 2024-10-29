"""
Author: daiji Kuriakose
Date:29-10-2024
Title:Python program to check weather the number is prime or not
"""
number=int(input("enter the number"))
isprime = True
for i in range(2,number//2+1):
    if number % i ==0:
        isprime = False
        break
if isprime:
    print(f"the given number {number} is prime")
else:
    print(f"the given number {number} is Not prime")