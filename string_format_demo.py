import csv

f = open('30oysters.csv', 'rb')
reader = csv.reader(f)
rownum = 0
for row in reader:
    if rownum == 0:
        header = row
        print "headers", header
    else:
        print map(float, row[0].split())

    rownum += 1
f.close()