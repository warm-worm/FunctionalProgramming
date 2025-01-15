names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']
print('Unsorted list:')
for name in names:
    print(name)
#key specifies function to be used for comparing the elements (lambda in this case)
sorted_names = sorted(names, key=lambda name: len(name)) 

print('')
print('Sorted list:')
for name in sorted_names:
    print(name)
