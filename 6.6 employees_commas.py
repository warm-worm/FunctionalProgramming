employees = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

employees_list = list(map(lambda employee: employee[0].upper() + ", " + employee[1], employees))

for e in employees_list:
    print(e)

