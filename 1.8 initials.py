name = input('Enter a name: ')
surname = input('Enter a surname: ')

initials = lambda name, surname: name[0].upper() + surname[0].upper()

print(f'Your initials are: {initials(name,surname)}')
