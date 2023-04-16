lst = [['a', 'c', 'd'],
       ['f', 'b', 'a'],
       ['a', 'n', 'k'],
       ['e', 'l', 'i']]

columns = [list(column) for column in zip(*lst)]

for column in columns:
    column.sort()

new_lst = [list(row) for row in zip(*columns)]

for row in new_lst:
    print(row)
