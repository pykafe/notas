import csv
b = open('cars.csv', 'w')
a = csv.writer(b)
data = [['Toyota', 'Prado', 'Avans'],\
        ['', '', ''],\
        ['', '', '']]
a.writerows(data)
b.close()
