#import operating system and csv
import os
import csv
#variables that holds multiple data (list)
TotalVotes = []
Canidates = []
CanidateVotes = []
#create path for csv file
csvpath = os.path.join("Resources", "election_data.csv")
#read through the csv path with reader
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    #loop through rows to find total number of votes
    for row in csvreader:
        TotalVotes.append(row[0])
        canidate = row[2]
        if canidate in Canidates:
            canidateindex = Canidates.index(canidate)
        else:
            Canidates.append(canidate)

#print putcomes to summary table
print(f"Total Votes: {len(TotalVotes)}")
print(f'{Canidates}')