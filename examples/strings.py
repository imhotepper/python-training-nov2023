name = 'george'
age = 40
balance = 128.5532

sentence = f'My name is {name.capitalize()} and my age next year is {age + 1}.'
print(sentence)
print(f"I have {balance:.2f}$ in my account.")

minutes = 150
print(str(minutes // 60) + " hours " + str(minutes % 60) + " minutes")
print(minutes // 60, "hours", minutes % 60, "minutes")
print(f"{minutes // 60} hours {minutes % 60} minutes")
