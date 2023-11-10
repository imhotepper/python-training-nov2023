name = 'george'
age = 40
balance = 128.5532

# Formatted strings (f-strings)
sentence = f'My name is {name.capitalize()} and my age next year is {age + 1}.'
print(sentence)
print(f"I have {balance:.2f}$ in my account.")

minutes = 150
print(str(minutes // 60) + " hours " + str(minutes % 60) + " minutes")
print(minutes // 60, "hours", minutes % 60, "minutes")
print(f"{minutes // 60} hours {minutes % 60} minutes")

# str.format method
sentence = 'My name is {1} and my age next year is {0}.'.format(age, name)
print(sentence)

values = [age, name]
sentence = 'My name is {1} and my age next year is {0}.'.format(*values)
print(sentence)

sentence = 'My name is {nm} and my age next year is {ag}.'.format(
    nm=name, ag=age)
print(sentence)

values = {"nm": name, "ag": age}
sentence = 'My name is {nm} and my age next year is {ag}.'.format(**values)
print(sentence)
