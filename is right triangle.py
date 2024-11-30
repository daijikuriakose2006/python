"""author: Daiji Kuriakose
   Date  : 30/11/2024
   Write a Python program to check weather the triangle is right triangle or not:"""
def is_right_triangle():
    side1=int(input("Enter the length of the first side"))
    side2=int(input("Enter the length of the second side"))
    side3=int(input("Enter the length of the third side"))
    list1=[side1,side2,side3]
    list1.sort()
    if list1[2]**2==list1[0]**2+list1[1]**2:
        print("The given sides are part of the right triangle")
    else:
        print("The given sides are not part of the right triangle")
is_right_triangle()