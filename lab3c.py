#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate'''
#Author ID: 162458210

def operate(number1, number2, operator):
    if operator == 'add':
        print(int(number1) + int(number2))
    elif operator == 'subtract':
        print(int(number1) - int(number2))
    elif operator == 'multiply':
        print(int(number1) * int(number2))
    elif operator == 'divide':
        print(int(number1) / int(number2))
    return 'Error: function operator can be "add", "subtract", "multiply" or "divide" '

if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))