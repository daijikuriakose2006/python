"""
created by Daiji Kuriakose
Date:19/11/2024
program to print different pattern
"""

#increasing triangle

no_of_lines=(int(input("Enter the number of lines")))
for i in range(no_of_lines+1):
    for j in range(i):
        print("*",end=" ")
    print()

#Decresing triangle

no_of_lines=(int(input("Enter the number of lines")))
for i in range(no_of_lines,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

#Hill pattern

no_of_lines=(int(input("Enter the number of lines")))
for i in range(no_of_lines + 1):
    for j in range(no_of_lines - i):
        print(" ",end=" ")
    for k in range(2 * i- 1):
        print("*",end=" ")
    print()

#Reverse hill pattern

no_of_lines = (int(input("Enter the number of lines")))
for i in range(no_of_lines,0,-1):
    for j in range(no_of_lines - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()