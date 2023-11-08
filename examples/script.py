"""This module exemplifies some basic Python concepts"""

print("hello world")

x = 10
print(x)

if x > 0:  # inline comment
    print("positive number")
    if x < 10:
        print("less than 10")

# explicit line joining
command = "/Users/iulia/PycharmProjects/python-training-nov2023/venv/bin/"\
          "python /Users/iulia/PycharmProjects/python-training-nov2023/"\
          "examples/script.py"
print(command)

# implicit line joining
my_shopping_list = [
    'apples',
    'bananas',
    'oranges',
    'pears',
    'peaches',
    'cherries',
]
print(my_shopping_list)

print(
    "Value of x is",
    x,
    "and value of my_shopping_list is",
    my_shopping_list
)

# multiline string
console_output = """Out[126]: 6.100000000000001
x % 10 + x // 10 % 10 + int( x/100 % 10)
Out[127]: 6"""

print(console_output)

str_with_newlines = "String on\ntwo lines"
print(str_with_newlines)

escape_newline = "String on\\ntwo lines"
print(escape_newline)

raw_string = r"String on\ntwo lines"
print(raw_string)
