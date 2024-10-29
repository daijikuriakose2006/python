"""
Author: daiji Kuriakose
Date:29-10-2024
Title:Python program to check weather the number is prime or not
"""
check_prime=int(input("Enter the number"))
for i in range(2,(check_prime//2)+1):
    if check_prime % i==0:
        break
if i==(check_prime//2):
    print(f"the given number {check_prime} is prime")
else:
    print(f"the number {check_prime} is not prime")