recorded_values = [48,47,54,50,42,68,39,46]

too_high = list(filter(lambda speed: speed > 50, recorded_values))

print(f"Recorded values: {', '.join(map(str, recorded_values))}")
print(f"Speed too high: {', '.join(map(str, too_high))}")
