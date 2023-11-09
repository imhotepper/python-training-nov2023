from datetime import date


class Person:
    count = 0  # class attribute (variable shared across instances)

    def __init__(self, name, date_of_birth):
        self.name = name  # instance attribute (specific to every instance)
        self.date_of_birth = date_of_birth
        Person.count += 1

    def greet(self, greeting="hi"):
        print(f"{greeting.capitalize()}! I am {self.name}!")


if __name__ == "__main__":
    p1 = Person("Anna", date(1989, 12, 4))
    p2 = Person(date_of_birth=date(1931, 6, 7), name="Mike")
    p3 = Person("Jane", date_of_birth=date(2004, 1, 5))

    print(p1.name, p2.name)
    print(Person.count, p1.count, p1.count is Person.count)

    p1.greet()
    p2.greet("hello")
