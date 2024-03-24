import math

def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: division by zero. You cannot divide by zero."
    
a = input("Enter a number. ")
b = input("Enter a second number. ")
try:
    a = int(a)
    b = int(b)
except ValueError:
    print("Error: invalid input. Please enter valid numbers.")
operation = input("Which operation would you like to perform? +, -, *, or /? ")
if operation == "+":
    print(addition(a, b))
elif operation == "-":
    print(subtraction(a, b))
elif operation == "*":
    print(multiplication(a, b))
elif operation == "/":
    print(division(a, b))
else:
    print("Sorry, that's not a valid operation.")