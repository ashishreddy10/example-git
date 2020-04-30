# our job is to read test.csv

import pandas as pd

filename = 'test.csv'
# / Users / ashishreddy / Desktop / exmaple - git / test.csv

read_file = pd.read_csv(filename)
print('looking at the first 5 lines of the file\n')
print(read_file.head())



print('looking at the last 5 lines of the file\n')
print(read_file.tail())









