'''
In This File we try to handle errors in Python using try and except blocks.
'''


def divide():
    try:
        # Attempt to convert inputs to integers
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        # Division function:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers.")
        return None
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    else:
        # This block will execute if no exceptions were raised in the try block.
        print("Division successful.")
        return result
    finally:
        # This block will execute regardless of whether an exception occurred or not.
        print("Execution completed.")

while True:
    # Call the divide function and store the result    
    result = divide()
    # If the result is not None, continue the loop
    if result is not None:
        print(f"Result: {result:.2f}")
        break
    else:
        print("Please try again...")
        continue
# ==================================================================================================