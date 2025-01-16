classification = [
    {"country":"Denmark","gold":2,"silver":4,"bronze":6},
    {"country":"Finland","gold":5,"silver":0,"bronze":4},
    {"country":"USA","gold":12,"silver":5,"bronze":11},
    {"country":"Peru","gold":0,"silver":1,"bronze":7}
]

countries = list(map(lambda x: x['country'], classification))
total_medals = list(map(lambda x: x['gold'] + x['silver'] + x['bronze'] , classification))

print('Total number of medals won by each country')
# Countries (x-axis) -> Total Medals (y-axis)

for i in range(len(countries)):
    print(f"{countries[i]}: {'*' * total_medals[i]}")
