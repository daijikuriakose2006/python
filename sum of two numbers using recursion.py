"""author: Daiji Kuriakose
   Date  : 3/12/2024
   Write a Python program to fint sum of two numbers using recursion:
   """
def add_numbers(n1,n2):
    if n2==0:
        return n1
    else:
        return add_numbers(n1+1,n2-1)
t=add_numbers(5,4)
print(t)