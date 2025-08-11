from time import sleep
from os import system


response = str(input("Want to enter: (Y)es or (N)o:")).upper()

system('cls'or 'clear'or 'ls')
if response == 'Y':
    print('\33[1;33m Loading the calculator \33[m')
    sleep(3)

while response == 'Y':

        arithmetic_operator = str(input("Expression arithmetic:"))
        system('cls'or 'clear'or 'ls')

        if arithmetic_operator == "+":
            first_number = float(input("Value:"))
            second_number = float(input("Other value:"))
            sum_number = first_number + second_number
            print("Sum of value is:",sum_number)

        elif arithmetic_operator == "-":
            first_number = float(input("Value:"))
            second_number = float(input("Other value:"))
            subtration_number = first_number - second_number
            print("Subtration of value is:",subtration_number)

        elif arithmetic_operator == "*":
            first_number = float(input("Value:"))
            second_number = float(input("Other value:"))
            multiplication_number = first_number * second_number
            print("Multiplicatio of value is:",multiplication_number)

        elif arithmetic_operator == "/":
            first_number = float(input("Value:"))
            second_number = float(input("Other value:"))
            division_number = first_number / second_number
            print("Division of value is:", division_number)

        elif arithmetic_operator == "**":
            first_number = float(input("Value:"))
            second_number = float(input("Other value:"))
            exponentiation = first_number ** second_number
            print("Exponentiation of value is:", exponentiation)

        elif arithmetic_operator == "//":
            first_number = float(input("Value:"))
            second_number = float(input("Other value:"))
            integer_division = first_number // second_number
            print("Integer Division of value is:", integer_division)
        
        exit_calculator = str(input("Want continue:")).upper()
        if exit_calculator == 'Y':
            print('\33[1;31mYour left the calculator\33[m')
            break

else:
    print("\33[1;31m Your din't want to enter the program \33[m")