import pandas as pd
import numpy as np

books = pd.read_csv('/home/benjadantes/Platzi/cursodePandasyNumpy/bestsellers.csv', sep=',')
#print(books)
#print(books.columns)
#print(books.index)
#print(books.Name)

'''
print(books[0:4])
print(books['Name'])
print(books[['Name', 'Author', 'Year']])
print(books.loc[0:7, ['Name', 'Author']])
print(books.loc[:, ['Author']] == 'JJ Smith')

print(books.iloc[0:3])
print(books.iloc[1,3])

#print(books.head(2))

books_2 = books.drop('Genre', axis=1)
#print(books_2.head(2))

#del books_2['Price']
#print(books_2)

books_2 = books_2.drop([0,1], axis=0)
print(books_2.head(2))

books_2['Hola'] = np.nan
print(books_2)

data = np.arange(0, books.shape[0])
print(data)

books['index'] = data
print(books)
'''

books.append(books)
print(books)