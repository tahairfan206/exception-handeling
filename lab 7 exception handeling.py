
# ArithmeticException equivalent -> ZeroDivisionError
try:
    num = 10
    result = num / 0
except ZeroDivisionError:
    print("ArithmeticException: Cannot divide by zero!")

# NullPointerException equivalent -> AttributeError or TypeError
try:
    obj = None
    print(len(obj))  # Trying to use None as an object
except TypeError:
    print("NullPointerException: Trying to access a property of a null object!")

# NumberFormatException equivalent -> ValueError
try:
    value = int("abc")  # Invalid integer conversion
except ValueError:
    print("NumberFormatException: Invalid number format!")

# ArrayIndexOutOfBoundsException equivalent -> IndexError
try:
    arr = [1, 2, 3]
    print(arr[5])  # Accessing index out of range
except IndexError:
    print("ArrayIndexOutOfBoundsException: Index out of range!")

print("\nProgram executed successfully with exception handling.")