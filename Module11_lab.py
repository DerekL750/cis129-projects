#exercise 9.1
with open('grades.txt', 'w') as grades:
    grades.write('97 100 1 74') 
    grades.write('57 100 2 74')
    grades.write('69 100 3 74')



#exercise 9.2

with open('grades.txt', 'r') as grades:
    for record in grades:
        individual_grade, total, count, average = record.split()
        grades.write(record)



#exercise 9.3

import csv

with open('grades.csv', mode='w', newline='') as account:
    writer = csv.writer(account)
    writer.writerow(['Derek Luna',80,96,88])