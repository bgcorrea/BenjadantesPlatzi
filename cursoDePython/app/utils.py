def get_population():
    keys = ['col', 'bol']
    values = [300, 400]
    return keys, values

A = 'hola'

def population_by_country(data, country):
    result = list(filter(lambda i: i['Country'] == country, data))
    return result

