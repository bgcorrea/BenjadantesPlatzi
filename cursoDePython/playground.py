'''
def message_creator(text):
    respuestas = {'computadora':'Con mi computadora puedo programar usando Python',  'celular': 'En mi celular puedo aprender usando la app de Platzi', 'cable': '¡Hay un cable en mi bota!' }
    if text in respuestas.keys():
        return respuestas[text]
    else:
        return 'Artículo no encontrado'

text = 'computadora'
response = message_creator(text)
print(response)
'''

a = {'1','2'}
b = {'2','3'}
print = (a & b)