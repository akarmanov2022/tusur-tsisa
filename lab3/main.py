import numpy as np
from prettytable import PrettyTable

data = np.array([
    [5, 9, 7, 2, 8, 3, 4, 1, 10, 6],
    [3, 8, 2, 1, 9, 10, 7, 6, 5, 4],
    [7, 2, 5, 6, 3, 4, 8, 10, 1, 9],
    [8, 1, 9, 7, 10, 4, 2, 5, 6, 3],
    [2, 9, 8, 7, 1, 3, 5, 4, 6, 10]])

table = PrettyTable(field_names=['А1', 'А2', 'А3', 'А4', 'А5', 'А6', 'А7', 'А8', 'А9', 'А10'])
table.add_rows(data)

print('Вариант 12.')
print(table)
