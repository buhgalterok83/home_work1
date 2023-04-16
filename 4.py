lst = [3.5, 2, 4, 6.2, 8]
new_lst = [lst[0]]

for i in range(1, len(lst)):
    avg = (lst[i] + lst[i-1]) / 2
    new_lst += [avg, lst[i]]

print(new_lst)
