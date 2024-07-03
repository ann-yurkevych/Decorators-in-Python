
#Task 1
def is_admin(func):
    def wrapper(user_type):
        if user_type != 'admin':
            raise ValueError("Permission denied")
        return func(user_type)
    return wrapper

@is_admin
def show_customer_receipt(user_type: str):
    # Very dangerous operation
    print("Showing customer receipt")

# Testing the function
try:
    show_customer_receipt('user')
except ValueError as e:
    print(e)  # Output: Permission denied

show_customer_receipt('admin')  # Output: Showing customer receipt

# Task 2

def catch_errors(func):
    def wrapper(data):
        try:
            return func(data)
        except Exception as e:
            print(f"Found 1 error during execution of your function: {type(e).__name__} {e}")
    return wrapper

@catch_errors
def process_user_data(user_data):
    # A risky operation
    print(f"Processing user: {user_data['name']}")
    print(f"Email: {user_data['email']}")

# Testing the function
process_user_data({'foo': 'bar'})
# Output: Found 1 error during execution of your function: KeyError 'name'

process_user_data({'name': 'Hanna Yu', 'email': 'hanna@gmail.com'})

# Task 3

def check_types(func):
    def wrapper(a, b):
        # Check argument types
        annotations = func.__annotations__
        if 'a' in annotations and not isinstance(a, annotations['a']):
            return f"Error: Argument a must be {annotations['a'].__name__}, not {type(a).__name__}"
        if 'b' in annotations and not isinstance(b, annotations['b']):
            return f"Error: Argument b must be {annotations['b'].__name__}, not {type(b).__name__}"

        # Call the function and check the return type
        result = func(a, b)
        if 'return' in annotations and not isinstance(result, annotations['return']):
            return f"Error: Return value must be {annotations['return'].__name__}, not {type(result).__name__}"

        return result

    return wrapper

@check_types
def add(a: int, b: int) -> int:
    return a + b

@check_types
def subtract(a: int, b: int) -> int:
    return a - b

@check_types
def multiply(a: int, b: int) -> int:
    return a * b

@check_types
def divide(a: int, b: int) -> float:
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Testing the functions
print(add(1, 2))  # Output: 3
print(add("1", "2"))  # Output: Error: Argument a must be int, not str

print(subtract(5, 3))  # Output: 2
print(subtract(5, "3"))  # Output: Error: Argument b must be int, not str

print(multiply(3, 4))  # Output: 12
print(multiply(3, "4"))  # Output: Error: Argument b must be int, not str

print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Error: Division by zero
print(divide(10, "2"))  # Output: Error: Argument b must be int, not str

