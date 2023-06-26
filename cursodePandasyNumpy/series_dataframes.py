import pandas as pd
psg = pd.Series(['Navas', 'Mbappe', 'Neymar', 'Messi'], index=[1, 7, 10, 30])
print(psg)

psg = pd.Series(['Navas', 'Mbappe', 'Neymar', 'Messi'])
print(psg)

psg = {1:'Navas', 7:'Mbappe', 10:'Neymar', 30:'Messi'}
print(psg)

print(psg[7])

dict = {'Jugador':['Navas', 'Mbappe', 'Neymar', 'Messi'],
        'Altura':[183.0, 180.0, 175.0, 165.0],
        'Goles':[2, 300, 200, 700]        
        }

print(dict)

psg_final = pd.DataFrame(dict, index=[1, 7, 10, 30])
print(psg_final)

print(psg_final.columns)
print(psg_final.index)
