X = 10


def func(a):
    b = 1

    def inner(c):
        d = 11

        # a = 0  # shadowing

        print("Built-in names (inner):", None, sum, len, int, dict)
        print("Global names (inner):", X, func, MyClass)
        print("Enclosing names (inner):", a, b, inner)
        print("Local names (inner):", c, d)

    inner(22)

    # sum = 0  # shadowing
    # X = 0  # shadowing

    global X  # access modifier
    X = 0

    print("Built-in names (func):", None, sum, len, int, dict)
    print("Global names (func):", X, func, MyClass)
    print("Local names (func):", a, b, inner)
    # print(globals(), locals())


class MyClass:
    pass


if __name__ == "__main__":
    # sum = 0  # shadowing

    func(2)

    print("Built-in names (global):", None, sum, len, int, dict)
    print("Global names (global):", X, func, MyClass)
