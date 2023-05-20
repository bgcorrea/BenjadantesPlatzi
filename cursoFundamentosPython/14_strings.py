text = 'Ella sabe programar en Python :)'

#IN

print('Javascript' in text)
print('Python' in text)

if 'Python' in text:
    print('Elegiste bien!!')
else:
    print('También elegiste bien')

#Len count the characters in the strings

size = len('amor')
print(size)

print(text.upper()) #mayusq
print(text.lower()) #minus
print(text.count('a')) #count
print(text.swapcase())
print(text.startswith('Ella'))
print(text.endswith('Rust'))
print(text.replace('Python', 'Java'))
print(text.replace('Ella', 'Él'))

text_2 = 'este es un título'
print(text_2)
print(text_2.capitalize()) #First letter in mayus
print(text_2.title()) #First letter of every word in mayus
print(text_2.isdigit()) # Ask if the string is a number
print('398'.isdigit())

text_js = text.replace('Python', 'JavaScript') # Create new variable
print(text_js)

