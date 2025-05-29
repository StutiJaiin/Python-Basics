#Write a Python program to use try-except-else block
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
else:
    print("Result is:", result)

#Write a Python program to use try-except-finally block
try:
    file = open("sample.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed")

#Write a Python program to write your own exception and throw it.
class MyException(Exception):
    pass

def check_value(x):
    if x < 0:
        raise MyException("Negative value not allowed")
    return x

x = int(input("Enter a number: "))
check_value(x)
print("Valid number:", x)


#Write a Python program to demonstrate the use of built in modules random and math.
import random
import math

x = random.randint(1, 100)
y = math.sqrt(x)

print("Random number:", x)
print("Square root:", y)

#Write a program to create a module and to use its functionality.
import mymodule

print(mymodule.add(5, 3))
print(mymodule.subtract(10, 4))

