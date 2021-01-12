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
        canidatename = row[2]
        if canidatename in Canidates:
            canidateindex = Canidates.index(canidatename)
            CanidateVotes[canidateindex] = CanidateVotes[canidateindex] + 1
        else:
            Canidates.append(canidatename)
            CanidateVotes.append(1)
#print putcomes to summary table
print(f"Total Votes: {len(TotalVotes)}")
print(f'{list(Canidates)} {CanidateVotes}')