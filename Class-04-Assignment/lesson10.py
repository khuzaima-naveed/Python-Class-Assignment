# #  Lesson 10: File Handling – All-in-One Example File

# # 🔹 1. Writing to a File

# print("🔸 Writing to a file")

# # 'w' mode creates a new file or overwrites an existing one
# with open("example.txt", "w") as file:
#     file.write("Hello, this is line one.\n")
#     file.write("This is line two.\n")

# print("✅ File written successfully.\n")

# # 🔹 2. Reading from a File

# print("🔸 Reading from a file")

# with open("example.txt", "r") as file:
#     content = file.read()
#     print("📄 File content:\n", content)


# # 🔹 3. Appending to a File

# print("🔸 Appending to a file")

# # 'a' mode adds data at the end of the file
# with open("example.txt", "a") as file:
#     file.write("This is an appended line.\n")

# print("✅ Line appended successfully.\n")


# # 🔹 4. Reading File Line-by-Line

# print("🔸 Reading file line-by-line")

# with open("example.txt", "r") as file:
#     for line in file:
#         print("📌", line.strip())


# # 🔹 5. Using try-except with File Handling

print("🔸 Handling file errors")

try:
    with open("nonexistent.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("❌ Error: File does not exist.")


# 🔹 6. Writing List of Strings to File

print("🔸 Writing a list to file")

lines = ["Apple\n", "Banana\n", "Cherry\n"]
with open("fruits.txt", "w") as file:
    file.writelines(lines)

print("✅ List of fruits written to 'fruits.txt'.\n")


# 🔹 7. Reading File into a List


print("🔸 Reading lines into a list")

with open("fruits.txt", "r") as file:
    fruits = file.readlines()

print("📋 Fruits List:")
print(fruits)  # Includes '\n'

# Optionally remove newline characters
cleaned_fruits = [fruit.strip() for fruit in fruits]
print("✅ Cleaned List:", cleaned_fruits)

