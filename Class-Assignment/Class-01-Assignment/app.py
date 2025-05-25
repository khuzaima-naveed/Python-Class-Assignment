# Python Data Types and Special Keywords

# Integer (int)
age = 25
print(type(age))  # <class 'int'>
print(age)        # 25

# Float (float)
price = 99.99
print(type(price))  # <class 'float'>
print(price)         # 99.99

# Complex (complex)
complex_number = 3 + 4j
print(type(complex_number))  # <class 'complex'>
print(complex_number)         # (3+4j)

# String (str)
name = "Khuzaima"
print(type(name))  # <class 'str'>
print(name)        # Khuzaima

# Boolean (bool)
is_logged_in = True
print(type(is_logged_in))  # <class 'bool'>
print(is_logged_in)        # True

# List (list)
fruits = ["apple", "banana", "mango"]
print(type(fruits))  # <class 'list'>
print(fruits)        # ['apple', 'banana', 'mango']

# Tuple (tuple)
coordinates = (10, 20)
print(type(coordinates))  # <class 'tuple'>
print(coordinates)        # (10, 20)

#Range (range)
numbers_range = range(1, 10, )
print(type(numbers_range))  # <class 'range'>
print(numbers_range)        # range(1, 10)

for i in range(1, 10, 2): 
  print(i)

# Set (set)
numbers = {1, 2, 3, 3}
print(type(numbers))  # <class 'set'>
print(numbers)        # {1, 2, 3}

# Frozenset (frozenset)
immutable_numbers = frozenset([1, 2, 3, 3])
print(type(immutable_numbers))  # <class 'frozenset'>
print(immutable_numbers)        # frozenset({1, 2, 3})         

# Dictionary (dict)
student = {"name": "Ali", "age": 20}
print(type(student))     # <class 'dict'>
print(student["name"])   # Ali
print(student["age"])    # 20


#🔸 Special Keywords with Examples


# None
result = None
print(type(result))  # <class 'NoneType'>
print(result)        # None

# True and False
print(10 > 5)   # True
print(10 < 3)   # False

# and, or, not
x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# is, is not
a = None
print(a is None)      # True
print(a is not None)  # False

# in, not in
fruits = ["apple", "banana"]
print("apple" in fruits)      # True
print("grape" not in fruits)  # True

# def and return
def greet():
    return "Hello!"

print(greet())  # Hello!

def square(x):
    return x * x

print(square(5))  # 25


# if, elif, else
age = 18
if age >= 18:
    print("Adult")  # Adult
elif age > 12:
    print("Teen")
else:
    print("Child")

# import
import math
print(math.sqrt(16))  # 4.0

