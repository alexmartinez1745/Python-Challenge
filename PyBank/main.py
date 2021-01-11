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
        averagechange = round(sum(Change) / len(Change), 2)
    #Finding greatest profit increase with max function
    HighestProfit = max(Change)
    #Finding greatest profit decrease wtih min function
    LowestProfit = min(Change)
    #Use an index to find the dates of when profit was the highest/lowest
    a = Change.index(HighestProfit)
    DateHighProfit = month [a + 1]
    b = Change.index(LowestProfit)
    DateLowProfit = month[b + 1]

print(f'Total Months: {len(month)}')        
print(f'Total: {sum(TotalMoney)}')
print(f'Average Change: {averagechange}')
print(f'Greatest Profit Increase: {DateHighProfit} ${HighestProfit}')
print(f'Greatest Profit Decrease: {DateLowProfit} ${LowestProfit}')
