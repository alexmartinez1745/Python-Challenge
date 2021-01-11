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
    for row in range(len(TotalMoney) - 1):
        Change.append(TotalMoney[row + 1] - TotalMoney[row])
        averagechange = sum(Change) / len(TotalMoney)
        #Finding greatest profit increase
        HighestProfit = max(Change)
        #Finding greatest profit decrease
        LowestProfit = min(Change)
print(f'Total Months: {len(month)}')        
print(f'Total: {sum(TotalMoney)}')
print(f'Change: {averagechange}')
print(f'Greatest Profit Increase: {HighestProfit}')
print(f'Greatest Profit Decrease: {LowestProfit}')
