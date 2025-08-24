# Simple Odd or Even Checker

def check_odd_even(number):
    """Check if a number is odd or even"""
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# Get input from user
try:
    num = int(input("Enter a number: "))
    result = check_odd_even(num)
    print(f"{num} is {result}")
except ValueError:
    print("Please enter a valid integer!")