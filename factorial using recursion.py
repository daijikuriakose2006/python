"""author: Daiji Kuriakose
   Date  : 22/10/2024
   Write a Python program to find factorial of a number using recursion:
   """
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
t=factorial(5)
print(t)