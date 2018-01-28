import inline as inline
import matplotlib
import openpyxl as openpyxl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
import xlrd as xlrd

data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
print('print data structure')
print(data)

football = pd.DataFrame(data, columns = ['year', 'team','wins','losses'])
print('print football data frame')
print(football)

from_csv = pd.read_csv('./data/mariano-rivera.csv');
print(from_csv.head())

cols = ['num', 'game', 'date', 'team', 'home_away', 'opponent',
        'result', 'quarter', 'distance', 'receiver', 'score_before',
        'score_after']

no_headers = pd.read_csv('./data/peyton-passing-TDs-2012.csv', sep=',', header=None, names=cols)
print(no_headers.head())

football.to_excel('./data/football.xlsx', index=False)
football2 = pd.read_excel('./data/football.xlsx')
print(football2)