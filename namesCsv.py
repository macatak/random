#!/usr/bin/python3

'''
simple CSV reader
will print out the row selected
or add it to a list to be used as part of a larger program
so just change it to the desired row
'''

# importing csv module
import csv

# csv file name
filename1 = "/home/zaphod/Downloads/lascon/names/baby-names.csv"
filename2 = "/home/zaphod/Downloads/lascon/names/surnames.csv"

# a list item
first_names = []

# reading csv file
with open(filename2) as f:
    # open the file which returns a pointer to the 1st line
    reader = csv.reader(f)
    # this will move the pointer to the next line so it skips the header line of the CSV
    next(reader)
    for row in reader:
        # print it
        #print(row[1])
        # add it to a list
        first_names.append(row[0])

for item in first_names:
    print(item)

print(first_names[10])
