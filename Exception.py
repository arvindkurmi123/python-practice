# ✅ EXCEPTION HANDLING (ERROR CONTROL)

try:
    x = int(input("Enter number: "))
    print(10 / x)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution 1 completed")

try:
    x = int(input("Enter number: "))
    print(10 / x)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution 1 completed")

try:
    x = int(input("Enter number: "))
    print(10 / x)
except (ValueError, ZeroDivisionError):
    print("## Please enter a valid number ##")
    print("## OR ##")
    print("## divide by zero ##")
finally:
    print("Execution completed")




# Enter number: a
# Please enter a valid number
# Execution 1 completed
# Enter number: 0
# Cannot divide by zero
# Execution 1 completed
# Enter number: b
# ## Please enter a valid number ##
# ## OR ##
# ## divide by zero ##
# Execution completed
