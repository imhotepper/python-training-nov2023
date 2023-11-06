name = 'george'
age = 40

sentence = f'My name is {name.capitalize()} and my age next year is {age + 1}.'
print(sentence)

minutes = 150
print(str(minutes // 60) + " hours " + str(minutes % 60) + " minutes")
print(minutes // 60, "hours", minutes % 60, "minutes")
print(f"{minutes // 60} hours {minutes % 60} minutes")
