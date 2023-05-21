with open('./text.txt', 'w+') as file: #w+ overwrite the text
    for line in file:
        print(line)
    file.write('Nuevas cosas en el archivo de texto \n otra linea \n y otra más')