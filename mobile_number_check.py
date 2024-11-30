def mobile_number():
    number=input("Enter number")
    if len(number)==10 and number[0] in '789':
        print("The mobile number is valid")
    else:
        print("The number is not valid")
mobile_number()