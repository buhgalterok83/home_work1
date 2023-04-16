lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
MIN = 3
MAX = 6

sum_ = 0
product = 1

for num in lst:
    if MIN <= num <= MAX:
        sum_ += num
        product *= num

print(f"sum_ = {sum_}, product = {product}")
