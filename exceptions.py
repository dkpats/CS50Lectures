import sys

try:
    x = int(input("Enter X: "))
    y = int(input("Enter Y: "))
except ValueError:
    print("Value Error: Something went wrong with you inputs.")
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x}/{y} = {result}")
