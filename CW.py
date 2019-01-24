def main():
    prob1()
    # prob2()
    # prob3()
    # prob4()

# Create a function in your program that counts from 0 to [NUMBER]
def prob1():
    number = int(input("Enter a number: "))
    counter(number)
def counter(num):
    for value in range(num+1):
        print(value)
#  Create a function that has a loop that quits with ‘q’.
#  If the user doesn't enter 'q', ask them to input another string.
def prob2():
    userInput = input("Enter a string\n")
    while userInput != "q":
        userInput = input("Great! Enter another string\n")
# Create 4 functions called add, subtract, multiply, and divide.
# Create them to allow the user to choose two numbers and preform all functions on these numbers.
def prob3():
    number1 =int(input("Enter your first number: "))
    number2 =int(input("Enter your second number: "))
    print(f'addition result: {add(number1, number2)}')
    print(f'multiplication result: {multiply(number1, number2)}')
    print(f'subtraction result: {subtract(number1, number2)}')
    print(f'division result: {divide(number1, number2)}')
def add(num1,num2):
    return num1 + num2
def multiply(num1,num2):
    return num1 * num2
def subtract(num1,num2):
    return num1 - num2
def divide(num1,num2):
    return num1/num2
# Create a function that will ask the user for a number.
# Use the function to get two numbers, then pass the two numbers to a function and
# ask a user if they want to add, subtract, multiple, or divide them.
# Return a string that prints the two numbers, which operation it did, and the result.
def prob4():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    operation = input("Do you want to add, subtract, multiply, or divide?\n").lower()
    print(operations(num1, num2, operation))
def operations(number1, number2, operation):
    if operation == "add":
        return (f'{number1} plus {number2} equals {number1+number2}')
    if operation == "multiply":
        return (f'{number1} times {number2} equals {number1*number2}')
    if operation == "subtract":
        return (f'{number1} minus {number2} equals {number1-number2}')
    if operation == "divide":
        return (f'{number1} divided by {number2} equals {number1//number2}')
    else:
        return("Invalid input")


if __name__ == '__main__':
    main()