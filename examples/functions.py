def greet(name: str, greeting: str = "hi"):
    print(f"{greeting.capitalize()}, {name}!")


greet("Anna")

my_name = "Iulia"
greet(my_name)

greet("John", "hello")  # positional arguments
greet(greeting="good morning", name="Jane")  # keyword arguments
greet("Ana", greeting="salut")  # mix of positional & keyword arguments


def decrement(nr, step=1):
    # print('inside func', id(nr))
    if step > 0:
        nr -= step  # nr = nr - step
        decremented = True
    else:
        nr += step  # nr = nr + step
        decremented = False

    # print('inside func, after decrement', id(nr))
    return nr, decremented


x, value_decremented = decrement(10)
print(x, value_decremented)

my_nr = 20
# print('outside func', id(my_nr))
result, dec = decrement(my_nr, 4)
print(my_nr, "was", "decremented" if dec else "incremented", "to", result)

my_nr = 20
result, dec = decrement(my_nr, -4)
print(my_nr, "was", "decremented" if dec else "incremented", "to", result)


def varargs(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs), end="\n\n")


varargs()
varargs(1)
varargs(1, 2, 3)

varargs(name="Anna")
varargs(1, 2, 3, name="Anna", age=20)
