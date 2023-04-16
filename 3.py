lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
MIN = 3
MAX = 6

sum_ = 0
product = 1
found = False

for num in lst:
    if MIN <= num <= MAX:
        found = True
        sum_ += num
        product *= num

if not found:
    sum_ = 0
    product = 0

print(sum_, product)
