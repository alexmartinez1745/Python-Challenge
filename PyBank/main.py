#import operating system and csv
import os
import csv
#crate variables that hold lists
month = []
TotalMoney = []
Change = [] 
HighestProfit = []
LowestProfit = []
#create path for csv file
csvpath = os.path.join("Resources", "budget_data.csv")
#reading through the csv path with reader..
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    budgetheader = next(csvreader)
    print("-----------------------------------------------")
    #looping through the rows to find total number of months
    for row in csvreader:
        #add to each month row to find total months
        month.append(row[0])
        #calculate total by summing up row 1
        TotalMoney.append(int(row[1]))
        #calculate changes per row of profit/loss and find the average
    for i in range(len(TotalMoney)-1):
        Change.append(TotalMoney[i+1] - TotalMoney[i])
print(f'Total Months: {len(month)}')        
print(f'Total: {sum(TotalMoney)}')
print(f'Change: {sum(Change)}')
