grade = 8

if grade == 10 or grade > 20:
    print('Wow! Maximum grade!')
elif grade >= 7:
    print('Good job!')
elif grade >= 5:
    print('You could have done better.')
else:
    print('Oh, no! :(')

match grade:
    case 10:
        print("Congrats!")
    case 9:
        print("You could have done better.")
    case 8 | 7:
        print("OKish")
    case _:
        print("Disappointing.")


while grade < 20:
    grade += 3
    print("Grade increased to", grade)


greeting = 'Bună dimineața'
for character in greeting:
    if character == 'a':
        continue
    print(character)

for item in greeting.encode("utf-8"):
    if item == 100:
        break
    print(item, end=" ")

print()
for i in range(5):
    print(i)

print()
for i in range(2, 10, 2):
    print(i)
