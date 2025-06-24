# The @my_decorator is a decorator that wraps the say_hello function.
# The wrapper function is a decorator that wraps the say_hello function.
# The wrapper function is a decorator that wraps the say_hello function.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

