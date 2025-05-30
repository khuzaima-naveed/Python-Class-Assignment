# 🐍 Lesson 05: Control Flow & Loops –

# ✅ CONDITIONAL STATEMENTS

# 1. If Statement
print("1. If Statement:")
age = 18
if age >= 18:
    print("You are eligible to vote.")
print()

# 2. If-Else Statement
print("2. If-Else Statement:")
num = 5
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
print()

# 3. If-Elif-Else 
print("3. If-Elif-Else:")
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")
print()


# 🔁 LOOPS

# 4. For Loop
print("4. For Loop:")
for i in range(5):
    print("Hello", i)
print()

# 5. While Loop
print("5. While Loop:")
count = 0
while count < 5:
    print("Count:", count)
    count += 1
print()

# 6. Nested Loops
print("6. Nested Loops:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
print()


# ⏭️ LOOP CONTROL STATEMENTS


# 7. Break Statement
print("7. Break Statement:")
for i in range(10):
    if i == 5:
        break
    print(i)
print()

# 8. Continue Statement
print("8. Continue Statement:")
for i in range(5):
    if i == 2:
        continue
    print(i)
print()


# 🔁 LOOP WITH ELSE

# 9. Else with For Loop
print("9. Else with For Loop:")
for i in range(3):
    print("Loop", i)
else:
    print("Loop completed!")


# 🐍 Lesson 06: Lists, Tuples & Dictionaries 

# 📋 LISTS

print("🔹 List Examples")

# 1. Creating a list
fruits = ['apple', 'banana', 'orange']
print("Fruits List:", fruits)

# 2. Accessing list items
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# 3. Adding an item to the list
fruits.append('mango')
print("After appending:", fruits)

# 4. Removing an item from the list
fruits.remove('banana')
print("After removing banana:", fruits)

# 5. Looping through a list
print("Looping through list:")
for fruit in fruits:
    print(fruit)

# 6. Checking if an item exists
print("Is 'apple' in list?", 'apple' in fruits)

# 7. List length
print("Number of fruits:", len(fruits))

# 8. List slicing
print("Sliced list (first two):", fruits[:2])


# 🔒 TUPLES

print("🔹 Tuple Examples")

# 1. Creating a tuple
colors = ('red', 'green', 'blue')
print("Colors Tuple:", colors)

# 2. Accessing tuple items
print("Second color:", colors[1])

# 3. Looping through a tuple
print("Looping through tuple:")
for color in colors:
    print(color)

# 4. Tuple length
print("Number of colors:", len(colors))

# 5. Tuple immutability
# colors[0] = 'yellow'  # ❌ This will raise an error (tuples are immutable)

# 📚 DICTIONARIES

print("🔹 Dictionary Examples")

# 1. Creating a dictionary
student = {
    "name": "Ali",
    "age": 20,
    "grade": "A"
}
print(student)

# 2. Accessing dictionary values
print("Student Name:", student["name"])

# 3. Changing a value
student["age"] = 21
print("Updated Age:", student["age"])

# 4. Adding a new key-value pair
student["passed"] = True
print("After adding 'passed':", student)

# 5. Removing a key-value pair
del student["grade"]
print("After removing 'grade':", student)

# 6. Looping through a dictionary
print("Looping through keys and values:")
for key, value in student.items():
    print(f"{key} → {value}")

# 7. Dictionary length
print("Number of items in student dictionary:", len(student))


# 🐍 Lesson 07: Set & Frozenset – All-in-One Example File

# 🔹 SETS

print("🔸 Set Examples")

# 1. Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# 2. Adding an element
my_set.add(6)
print("After adding 6:", my_set)

# 3. Removing an element
my_set.remove(2)
print("After removing 2:", my_set)

# 4. Discarding an element (no error if not found)
my_set.discard(100)  # No error
print("After discarding 100 (not in set):", my_set)

# 5. Set cannot have duplicate values
duplicate_set = {1, 2, 2, 3}
print("Set with duplicates (removed automatically):", duplicate_set)

# 6. Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a.union(b))
print("Intersection:", a.intersection(b))
print("Difference (a - b):", a.difference(b))
print("Symmetric Difference:", a.symmetric_difference(b))

# 7. Looping through a set
print("Looping through a set:")
for item in my_set:
    print(item)

# 8. Set length
print("Length of set:", len(my_set))

# 🔹 FROZENSET

print("🔸 Frozenset Examples")

# 1. Creating a frozenset
frozen = frozenset([1, 2, 3, 4])
print(frozen)

# 2. Trying to add or remove (will cause an error)
# frozen.add(5)     ❌ Not allowed
# frozen.remove(2)  ❌ Not allowed

# 3. Set operations with frozenset
f1 = frozenset([1, 2, 3])
f2 = frozenset([3, 4, 5])

print("Union:", f1 | f2)
print("Intersection:", f1 & f2)
print("Difference:", f1 - f2)
print("Symmetric Difference:", f1 ^ f2)

# 4. Looping through frozenset
print("Looping through frozenset:")
for item in frozen:
    print(item)

# 5. Frozenset length
print("Length of frozenset:", len(frozen))
