def increment(x):
    return x + 1

increment_v2 = lambda x : x + 1 #Anonymmous function

result = increment_v2(20)
print(result)

full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'

text = full_name('nicolas', 'perez casas')
print(text)