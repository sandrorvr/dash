import sqlite3
import pandas as pd
import numpy as np

data = pd.read_csv('db.csv')
data.fillna('null', inplace=True)


def criarReferenciaTab(data):
    ref = {}
    for i in range(len(data.columns)):
        if type(data.iloc[0,i]) == str:
            ref[data.columns[i]] = 'text'
        else:
            ref[data.columns[i]] = 'integer'

    ref['id'] = 'integer'
        
    return ref


#dicRef = criarReferenciaTab(data)


def criarStringCREATE(ref, tableName):
    string = f'CREATE TABLE {tableName} ('
    for key in ref.keys():
        string = string + f'{key} {ref[key]},'
    
    string = list(string)
    string[-1] = ')'

    return ''.join(string)


#print(criarStringCREATE(dicRef, 'DADOS'))


def popularTab(data, tableName, values, index):
    string = f'INSERT INTO {tableName} VALUES ('
    
    for val in values:
        if type(val) == str:
            string = string + f'\"{val}\",'
        else:
            string = string + f'{str(val)},'
        
    string = string + str(index) + ','
    
    string = list(string)
    string[-1] = ')'
    
    return ''.join(string)



#print(popularTab(data, 'DADOS', data.iloc[0,:].values))
    


dicRef = criarReferenciaTab(data)

connection = sqlite3.connect('db.sqlite3')
c = connection.cursor()

c.execute(criarStringCREATE(dicRef, 'DADOS'))

for i in range(len(data)):
    c.execute(popularTab(data, 'DADOS', data.iloc[i,:].values, i))

connection.commit()
connection.close()
