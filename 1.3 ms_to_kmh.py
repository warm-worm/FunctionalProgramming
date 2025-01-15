def ms_to_kmh(ms):
    return int(ms * 18/5)

ms = int(input('Enter the speed in miles per second: '))

print(f'The speed of {ms}m/s is {ms_to_kmh(ms)}km/h.')
