test_results = [
   {"name":"Peter","result":27},
   {"name":"Anna","result":63},
   {"name":"Robert","result":92},
   {"name":"Paul","result":46},
   {"name":"Barbara","result":52}]

score_between = list(filter(lambda student: student["result"]>=50 and student["result"]<=70, test_results))

print('Students whose scores are between 50 and 70 points:')
for student in score_between:
    print(f'{student["name"]} ({student["result"]} points)')