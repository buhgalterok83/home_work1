numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

divisible_by_3_not_5 = []
divisible_by_5_not_3 = []
divisible_by_3_and_5 = []

for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        divisible_by_3_and_5.append(num)
    elif num % 3 == 0:
        divisible_by_3_not_5.append(num)
    elif num % 5 == 0:
        divisible_by_5_not_3.append(num)

print("Числа, которые делятся только на 3, но не на 5:", divisible_by_3_not_5)
print("Числа, которые делятся только на 5, но не на 3:", divisible_by_5_not_3)
print("Числа, которые делятся и на 3, и на 5:", divisible_by_3_and_5)
