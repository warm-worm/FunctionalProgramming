from functools import reduce

numbers = [2,4,6,3,7,5]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

sum_of_even = reduce(lambda x, y: x + y, numbers)

print(sum_of_even)