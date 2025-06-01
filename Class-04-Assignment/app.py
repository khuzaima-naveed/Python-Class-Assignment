# 🐍 Lesson 08: Control Modules & Functions – All-in-One Example File

# 🔹 FUNCTIONS IN PYTHON

print("🔸 Function Examples")

# 1. Basic function without parameters
def greet():
    print("Hello! Welcome to Python Functions.")

greet()  # Calling the function

# 2. Function with parameters
def add(a, b):
    return a + b

result = add(10, 5)
print("Addition result:", result)

    # 3. Function with default parameters
def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user("Khuzaima")
greet_user()  # Uses default value

# 4. Function with return value
def square(num):
    return num * num

print("Square of 4:", square(4))

# 5. Keyword arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=22, name="Ali")

# 6. Arbitrary arguments (*args)
def print_numbers(*nums):
    for n in nums:
        print(n, end=" ")
    print()

print("Multiple numbers:")
print_numbers(1, 2, 3, 4, 5)

# 7. Arbitrary keyword arguments (**kwargs)
def user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print("User Info:")
user_info(name="Ayesha", age=20, city="Lahore")

# 8. Nested functions
def outer():
    print("This is the outer function.")
    
    def inner():
        print("This is the inner function.")
    
    inner()

outer()

# 9. Lambda functions
double = lambda x: x * 2
print("Double of 5 using lambda:", double(5))

# 10. Positional-only arguments
def posFun(x, y, /, z):
    print(x + y + z)

print("Evaluating positional-only arguments: ")
posFun(1, 2, z=3)

# uncomment to see error
#posFun(x=1, y=2, z=3)

# 11. Generator Function

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for number in count_up_to(5):
    print("Generated number:", number)

# # 12. Recursive Function

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))



# 🔹 MODULES IN PYTHON

print("🔸 Module Examples")

# Built-in module example
import math

print("Square root of 16 is", math.sqrt(16))
print("Value of PI:", math.pi)

# Importing specific function from module
from math import pow

print("3 raised to power 4:", pow(3, 4))

#Renaming a module (aliasing)
import random as rnd

print( rnd.randint(1, 10))

# Creating a custom module
import mymodule
print(mymodule.say_hello("Khuzaima"))

#Using dir() to explore module attributes
import math
print("Functions in math module:")
print(dir(math))  # Lists all attributes/functions in math module

