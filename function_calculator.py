print("Welcome to the function Calculator!")
def add():    
    try:
        num_add = int(input("PLease enter a number for sum: "))
        num_add2 = int(input("PLease enter a second number for sum: "))
        print(num_add + num_add2)
    except ValueError:
            print("That's not a number, Try again!")
def subtract():
    try:
        num_sub = int(input("PLease enter a number to subtract: "))
        num_sub2 = int(input("PLease enter a second number to subtract: "))
        print(num_sub - num_sub2)
    except ValueError:
            print("That's not a number, Try again!")
def multiply():
    try:
        num_mult = int(input("Please enter a number to find the product: "))
        num_mult2 = int(input("Please enter a number to find the product: "))    
        print(num_mult * num_mult2)
    except ValueError:
            print("That's not a number, Try again!")
def divide():
    try:
        num_div = int(input("Please enter a number to divide: "))
        num_div2 = int(input("Please enter a second number to divide: "))
        print(num_div / num_div2)
    except ZeroDivisionError:
            print("The number cannot be divided by Zero!")
add()
subtract()
multiply()
divide()   
