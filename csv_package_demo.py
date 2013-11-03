import csv

if __name__ == "__main__":
    f = open('30oysters.csv', 'rb')
    reader = csv.reader(f)

    rownum = 0
    for row in reader:
        if rownum == 0:
            header = row
        else:
            print row
        rownum += 1

    f.close()