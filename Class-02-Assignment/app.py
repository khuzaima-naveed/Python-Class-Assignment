#1. Arithmetic Operators
a = 10
b = 3

print("Addition (a + b) =", a + b)        # 13
print("Subtraction (a - b) =", a - b)     # 7
print("Multiplication (a * b) =", a * b)  # 30
print("Division (a / b) =", a / b)        # 3.333...
print("Floor Division (a // b) =", a // b) # 3
print("Modulus (a % b) =", a % b)         # 1
print("Exponent (a ** b) =", a ** b)      # 1000

# 2. Assignment Operators

x = 5
print("Initial x =", x)

x += 2  # x = x + 2
print("x += 2 =", x)

x -= 1  # x = x - 1
print("x -= 1 =", x)

x *= 3  # x = x * 3
print("x *= 3 =", x)

x /= 2  # x = x / 2
print("x /= 2 =", x)

x %= 2  # x = x % 2
print("x %= 2 =", x)

x = 4
x **= 2  # x = x ** 2
print("x **= 2 =", x)

x //= 3  # x = x // 3
print("x //= 3 =", x)

#✅ 3. Comparison Operators

a = 5
b = 10

print("a == b:", a == b)   # False
print("a != b:", a != b)   # True
print("a > b:", a > b)     # False
print("a < b:", a < b)     # True
print("a >= b:", a >= b)   # False
print("a <= b:", a <= b)   # True

#4. Logical Operators

x = True
y = False

print("x and y =", x and y)   # False
print("x or y =", x or y)     # True
print("not x =", not x)       # False

#5. Identity Operators

a = [1, 2]
b = [1, 2]
c = a

print("a is b:", a is b)       # False (different memory)
print("a == b:", a == b)       # True (same content)
print("a is c:", a is c)       # True (same memory)
print("a is not b:", a is not b)  # True

#6. Membership Operators

numbers = [1, 2, 3, 4]

print("2 in numbers:", 2 in numbers)      # True
print("5 not in numbers:", 5 not in numbers)  # True

#7. Bitwise Operators

a = 5      # 0101 in binary
b = 3      # 0011 in binary

print("a & b =", a & b)   # 1  => 0001
print("a | b =", a | b)   # 7  => 0111
print("a ^ b =", a ^ b)   # 6  => 0110
print("~a =", ~a)         # -6 (bitwise NOT)
print("a << 1 =", a << 1) # 10 (shift left)
print("a >> 1 =", a >> 1) # 2 (shift right)
