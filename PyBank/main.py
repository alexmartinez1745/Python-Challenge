#import operating system and csv
import os
import csv
#create path for csv file
csvpath = os.path.join("Resources", "budget_data.csv")
#reading through the csv path with reader..
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    budgetheader = next(csvreader)
    print("-----------------------------------------------")
    month = []
    #looping through the rows to find total number of months
    for row in csvreader:
        month.append(row[0])
        print((len(month)))