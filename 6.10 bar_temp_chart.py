temps = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

cities = list(map(lambda x: x, temps.keys()))
temp_values = list(map(lambda x: temps[x], temps.keys()))

print('Temperatures recorded in cities:')
#Cities (x-axis) -> Temperatures (y-axis)#

for i in range(len(cities)):
    print(f"{cities[i]}: {'*' * temp_values[i] if temp_values[i] > 0 else ''}")
