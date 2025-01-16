# For a 500ml bottle, the allowable tolerance is 2%
last_10_bottles = [508,500,512,499,492,511,503,476,501,509]
capacity = 500
tolerance = 2

lower_limit = capacity - (capacity * tolerance / 100)
upper_limit = capacity + (capacity * tolerance / 100)

def incorrectly_filled(bottle):
    return bottle < lower_limit or bottle > upper_limit

incorrect_bottles = list(filter(incorrectly_filled, last_10_bottles))

incorrect_percentage = (len(incorrect_bottles) / len(last_10_bottles)) * 100

print(f'Bottle capacity:    {capacity}ml')
print(f'Filling tolerance:  {tolerance}%')
print(f"Filled bottles:     {','.join(map(str, last_10_bottles))}")
print(f'Incorrectly filled: {incorrect_percentage:.0f}%')
