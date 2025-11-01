with open('diaries.txt', 'w') as file:
    file.write('I am 23 years old.\nI live in Kandy.\nI study Python')

with open('diaries.txt', 'r') as file:
    file.seek(10)
    content = file.read()
    print(content)
