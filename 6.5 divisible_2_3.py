numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

divisible = list(filter(lambda x: x%2 == 0 and x%3 == 0 ,numbers))

print(divisible)
