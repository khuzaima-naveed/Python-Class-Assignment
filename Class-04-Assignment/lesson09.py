# #  Lesson 09: Exception Handling 

# # 🔹 1. The try Block

# print("🔸 1. The try Block")

# try:
#     num = int(input("Enter a number to divide 10: "))
#     result = 10 / num
#     print("Result is:", result)
# except:
#     print("An error occured")  # This block will run if there's an error


# # 🔹 2. The except Block (Handling Specific Errors)

# print("🔸 2. The except Block")

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print("Result is:", result)
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
# except ValueError:
#     print("Error: Please enter a valid integer.")



# # 🔹 3. The else Block


# print("🔸 3. The else Block")

# try:
#     num = int(input("Enter a number (non-zero): "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
# except ValueError:
#     print("Error: Invalid input.")
# else:
#     print("Success! Result is:", result)

# # 🔹 4. The finally Block

# print("🔸 4. The finally Block")

# try:
#     name = input("Enter your name: ")
#     if name == "":
#         raise ValueError("Name cannot be empty.")
#     print(f"Welcome, {name}!")
# except ValueError as e:
#     print("Caught an exception:", e)
# finally:
#     print("This block always runs. ✅")


# # 🔹 5. A complete Example 

def divide_numbers():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = a / b
    except ZeroDivisionError:
        print("❌ You can't divide by zero.")
    except ValueError:
        print("❌ Invalid input. Please enter integers only.")
    else:
        print("✅ Division successful! Result =", result)
    finally:
        print("✅ Operation complete.")

divide_numbers()
