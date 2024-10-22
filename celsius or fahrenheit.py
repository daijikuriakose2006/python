"""author: Daiji Kuriakose
   Date  : 22/10/2024
   Write a Python program to convert Celsius to Fahrenheit and vise versa:"""
temp=float(input("enter the temperature"))
scale=input("Is this in (C)elsius or (F)ahrenheit?")
if scale=='C':
    f=(9/5*temp)+32
    print(temp,"Degree celsius is",f,"Degree fahrenheit.")
else:
    c=(5/9)*(temp-32)
    print(temp,"degree fahrenheit is",c,"Degree celsius.")