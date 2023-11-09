import functools


def decorator(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print("I got decorated", args, kwargs)
        result = func(*args, **kwargs)  # func = ordinary, greet
        print("After function call")
        return result
    return inner


@decorator
def ordinary():
    print("I am ordinary")


# ordinary = decorator(ordinary)
# print(ordinary)

ordinary()  # decorator.<locals>.inner()


@decorator
def greet(name: str, greeting: str = "hi"):
    print(f"{greeting.capitalize()}, {name}!")


greet("Anna")  # decorator.<locals>.inner("Anna")
greet("Anna", greeting="hello")  # decorator.<locals>.inner("Anna", greeting="hello")


@decorator
def add(a, b):
    """Simple function to add two numbers together"""
    return a + b


print("Result of add(15, 13):", add(15, 13))
print(add, add.__name__, add.__doc__)
