distance = int(input('Enter the distance in km: '))
hours = int(input('Enter the number of travel hours: '))
minutes = int(input('Enter the number of travel minutes: '))

def avg_speed(distance,hours,minutes):
    return round(distance / (hours + minutes/60), 1)

print(f'Average speed: {avg_speed(distance,hours,minutes)} km/h')
