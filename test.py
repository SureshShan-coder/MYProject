try:
    number = int(input("Enter a number: "))  # Get input from the user
    if number == 0:
        # Manually raise a ValueError if the number is negative
        raise ValueError("Error: The number cannot be negative.")
    result = 10 / number  # Perform division
except ValueError as ve:
    print(ve)  # Handle invalid input or negative number error
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")  # Handle division by zero
else:
    print(f"Result: {result}")  # Execute only if no exceptions are raised
finally:
    print("Execution of try-except block is complete.")  # Always execute