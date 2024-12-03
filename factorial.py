"""author: Daiji Kuriakose
   Date  : 3/12/2024
   Write a Python program to find factorial using recursion:
"""
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)
factorial(5)