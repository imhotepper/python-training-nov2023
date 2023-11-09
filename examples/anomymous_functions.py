def compute(a, b, operation):
    return operation(a, b)


def my_func(x, y):
    return x ** 2 + y * 7


print(compute(10, 2, pow))
print(compute(10, 2, my_func))
print(compute(10, 2, lambda x, y: x + y))
print(compute(10, 2, lambda x, y: x * 2 + y // 2))
