import csv

with open("customers.csv", "r") as og:
    read = csv.reader(og)

    with open("coustomer_country.csv", "w") as new:
        write = csv.writer(new)
        for column in read:

            write.writerow((column[1], column[2], column[4]))
