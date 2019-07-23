#!/usr/bin/python3

'''
simple CSV reader
will print out the row selected
or add it to a list to be used as part of a larger program
so just change it to the desired row
'''

# importing csv module
import csv

def read_csv(csvFilename, row_number):
    # list object to return
    return_list = []
    with open(csvFilename) as f:
        # open the file which returns a pointer to the 1st line
        reader = csv.reader(f)
        # this will move the pointer to the next line so it skips the header line of the CSV
        next(reader)
        for row in reader:
            # print it if you want
            # print(row[row_number])
            # add it to a list
            return_list.append(row[1])
    return return_list

if __name__ == '__main__':
    # csv file name
    filename1 = "/home/zaphod/Downloads/lascon/names/baby-names.csv"
    filename2 = "/home/zaphod/Downloads/lascon/names/surnames.csv"
    firstNameList = read_csv(filename1, 1)
    lastNameList = read_csv(filename2, 0)
    print(len(firstNameList))
    print(len(lastNameList))
