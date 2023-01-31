import csv

with open('EmployeePay.csv', 'r') as input_file:

    reader = csv.reader(input_file)

    for row in reader:
        department = row[0]
        first_name = row[1]
        last_name = row[2]
        salary = row[3]
        bonus = row[4]

        print(f"Department: {department}")
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Salary: {salary}")
        print(f"Bonus: {bonus}")
        print()
