"""
Author: daiji Kuriakose
Date:29-10-2024
Title:Python program to print n prime numbers
"""
limit=int(input("enter the number"))
for number in range (2,limit+1):
    isprime=True
    for i in range (2,(number//2)+1):
        if number % i==0:
            isprime = False
            break
    if isprime:
         print(number)
