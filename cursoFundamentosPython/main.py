import random

options = ('piedra', 'papel', 'tijeras')
computer_wins = 0
user_wins = 0
rounds = 1

while True:
    print('*' *10)
    print('ROUND', rounds)
    print('*' * 10)
    
    
    user_option = input('piedra, papel o tijeras => ')
    user_input  = user_option.lower()
    computer_option = random.choice(options)

    if not user_option in options:
        print('Por favor escoge una opción correcta para poder jugar')
        continue

    print('User Option = >', user_option)
    print('Computer Option = >', computer_option)

    if not user_option in options:
        print('Partida no válida')


    if user_input == computer_option:
        print('Es un empate!')
    elif user_input == 'piedra':
        if computer_option == 'tijeras':
            print('Piedra gana a tijeras')
            print('El usuario gana la partida')
            user_wins +=1
        else:
            print('Papel gana a piedra')
            print('La computadora gana la partida')
            computer_wins +=1
    elif user_input == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a la piedra')
            print('El usuario gana la partida')
            user_wins +=1
        else:
            print('Tijeras ganan a papel')
            print('La computadora gana la partida')
            computer_wins += 1
    elif user_input == 'tijeras':
        if computer_option == 'papel':
            print('Tijeras ganan a papel')
            print('El usuario gana la partida')
            user_wins +=1

        else:
            print('Piedra gana a las tijeras')
            print('La computadora gana la partida')
            computer_wins += 1
            
    print('El usuario lleva ', user_wins, 'puntos')
    print('El computador lleva ', computer_wins, 'puntos')
    rounds +=1
    
    if computer_wins == 2:
        print('El ganador es la computadora')
        break
    if user_wins == 2:
        print('El ganador es el usuario')
        break

'''
import random

def choice(a):
    if a == 1:
        return('Piedra')
    elif a == 2:
        return('Papel')
    elif a == 3:
        return('Tijeras')
    else:
        return('Perder')

def tex():
    print(f'\n Has elegido: {choice(usuario)}')
    print(f'El PC ha elegido: {choice(pc)}\n')
    
print('\n ¡Cachipún! \n')
usuario = int(
    input('ingrese: \n1 para Piedra \n2 para Papel \n3 para Tijeras => '))
pc = random.randint (1, 3)
if pc == usuario:
    tex()
    print('Empate')
elif (usuario == 1 and pc == 3) or (usuario == 2 and pc == 1) or (usuario == 3 and pc == 2):
    tex()
    print('Has ganado! :)')
elif usuario not in range(1, 3):
    tex()
    print('Por favor selecciona dentro de las opciones señaladas anteriormmente')
else:
    tex()
    print('Has perdido :(')
    
✂️
🪨 
📄
🎖️
🤖
🙋

'''
