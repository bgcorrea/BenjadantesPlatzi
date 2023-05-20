import random

print("""
    [📄🪨✂️ Bienvenid@ al juego Piedra, Papel o tijera 📄🪨✂️]
                    >>> Ingresa una opción <<<  """)


def choosing_avatar(text):
    option_player = {1:'👨', 2:'👩', 3:'🧑'}
    if text in option_player.keys():
        return option_player[text]
    else:
        return None
    
response = None
while not response:
    text = input('Elige un Avatar:\n1. 👨\n2. 👩 \n3. 🧑 \n =>')
    response = choosing_avatar(int(text))
    if not response:
        print('Opción inválida. Por favor elige un número del 1 al 3')
print('Has elegido', response)


def choose_option():
    options = ('piedra', 'papel', 'tijeras')
    user_option = input('piedra, papel o tijeras => ')
    user_option  = user_option.lower()
    
    if not user_option in options:
        print('Por favor escoge una opción correcta para poder jugar')
        # continue
        return None, None

    computer_option = random.choice(options)

    print('User Option = >', user_option)
    print('Computer Option = >', computer_option)
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Es un empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijeras':
            print('🪨 Piedra gana a tijeras ✂️')
            print('El usuario gana la partida')
            user_wins +=1
        else:
            print('📄 Papel gana a piedra 🪨')
            print('La computadora gana la partida')
            computer_wins +=1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('📄 Papel gana a la piedra 🪨')
            print('El usuario gana la partida')
            user_wins +=1
        else:
            print('✂️ Tijeras ganan a papel 📄')
            print('La computadora gana la partida')
            computer_wins += 1
    elif user_option == 'tijeras':
        if computer_option == 'papel':
            print('✂️ Tijeras ganan a papel')
            print('El usuario gana la partida')
            user_wins +=1
        else:
            print('🪨 Piedra gana a las tijeras ✂️')
            print('La computadora gana la partida')
            computer_wins += 1
    return user_wins, computer_wins
    
def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print('*' *10)
        print('ROUND', rounds)
        print('*' * 10)
        
        print('El usuario lleva ', user_wins, 'puntos')
        print('El computador lleva ', computer_wins, 'puntos')
        
        rounds +=1
        
        user_option, computer_option = choose_option()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        
        if computer_wins == 2:
            print('El ganador es el computador 🤖')
            break
        
        if user_wins == 2:
            print(f'El ganador es el usuario {response}')
            break
run_game()