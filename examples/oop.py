from datetime import date


class Person(object):
    count = 0  # class attribute (variable shared across instances)
    MAX_YEAR = 1900

    def __init__(self, name, date_of_birth):
        self.name = name  # instance attribute (specific to every instance)
        self._date_of_birth = date_of_birth
        self._increment_count()

    @property
    def date_of_birth(self):  # getter
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value: date):  # setter
        if value.year <= self.MAX_YEAR:
            raise ValueError(f"Year should be greater than {self.MAX_YEAR}")
        self._date_of_birth = value

    @date_of_birth.deleter
    def date_of_birth(self):  # deleter
        pass

    @property
    def age(self):  # computed attribute
        return self.compute_age(self._date_of_birth)

    def greet(self, greeting="hi"):  # instance method
        print(f"{greeting.capitalize()}! I am {self.name}!")

    @classmethod
    def _increment_count(cls):  # class method
        cls.count += 1

    @staticmethod
    def compute_age(date_obj):  # static method
        diff = date.today() - date_obj
        return round(diff.days / 365.25)

    def __str__(self):
        return f"Person (name={self.name}; date_of_birth={self._date_of_birth})"

    def __add__(self, other):
        return Person(self.name, other.date_of_birth)


class Student(Person):
    def __init__(self, name, date_of_birth, university):
        super().__init__(name, date_of_birth)
        self.university = university

    def __str__(self):
        return (f"Student (name={self.name}; "
                f"date_of_birth={self._date_of_birth}; "
                f"university={self.university})")

    def get_grade(self, subject):
        return 8


if __name__ == "__main__":
    p1 = Person("Anna", date(1989, 12, 4))
    p2 = Person(date_of_birth=date(1931, 6, 7), name="Mike")
    p3 = Person("Jane", date_of_birth=date(2004, 1, 5))

    print("Persons ages:", p1.age, p2.age, p3.age)

    print(p1.name, p2.name)
    print(Person.count, p1.count, p1.count is Person.count)

    p1.greet()
    p2.greet("hello")

    print(p1.__dict__)
    print(dir(p1))

    print(p1, repr(p1))

    p4 = p1 + p2  # p4 = p1.__add__(p2)
    print(p4)

    print(Person.count)

    print(
        Person.compute_age(p1.date_of_birth),
        Person.compute_age(date(1691, 5, 3)),
    )

    # Person._increment_count()  # access to a protected member of the class

    print(p1.date_of_birth)  # get date_of_birth
    try:
        p1.date_of_birth = date(1800, 2, 23)  # set date_of_birth
    except ValueError as ex:
        print(ex)
    del p1.date_of_birth  # delete date_of_birth
    print(p1.date_of_birth)

    print("Age before set date_of_birth", p1.age)
    p1.date_of_birth = date(1988, 12, 4)
    print("Age after set date_of_birth", p1.age)

    s1 = Student("Jane Smith", date(2004, 1, 5), "Politehnica București")
    print(s1)
    print(s1.get_grade("Math"))
