#import operating system and csv
import os
import csv
#variables that holds multiple data (list)
TotalVotes = []
Canidates = []
CanidateVotes = []
percentagevotes = []
percent = 0
Winner = []
maxvotes = 0
#create path for csv file
csvpath = os.path.join("Resources", "election_data.csv")
#read through the csv path with reader
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    #loop through rows to find total number of votes
    for row in csvreader:
        TotalVotes.append(row[0])
        #set variable to find different canidate names in row 2 of csv
        canidatename = row[2]
        #create conditional to find unique canidate name and add each vote
        #if not in current canidate move to the next canidate
        if canidatename in Canidates:
            canidateindex = Canidates.index(canidatename)
            CanidateVotes[canidateindex] = CanidateVotes[canidateindex] + 1
        else:    
            Canidates.append(canidatename)
            CanidateVotes.append(1)
            #Find winner with max function in voter index
            Winner = Canidates[CanidateVotes.index(max(CanidateVotes))]
    #Calculate percent of votes with range of canidates
    for votecount in range(len(Canidates)):
        percent = round(((CanidateVotes[votecount]) / (len(TotalVotes))) * 100 , 2)
        percentagevotes.append(percent)

#print putcomes to summary table
print("Election Results")
print("-----------------------")
print(f"Total Votes: {len(TotalVotes)}")
print("-----------------------")
print(f'{Canidates[0]}: {percentagevotes[0]}% ({CanidateVotes[0]}) ')
print(f'{Canidates[1]}: {percentagevotes[1]}% ({CanidateVotes[1]}) ')
print(f'{Canidates[2]}: {percentagevotes[2]}% ({CanidateVotes[2]}) ')
print(f'{Canidates[3]}: {percentagevotes[3]}% ({CanidateVotes[3]}) ')
print("-----------------------")
print(f"Winner: {Winner}")
print("-----------------------")


#create path for text file
textpath = os.path.join("Analysis", "SummaryAnalysis.txt")
output = open(textpath, "w")
#write text same was as reader just move into writer format and use \n to form new line
output.write("Election Results\n")
output.write("-----------------------\n")
output.write(f"Total Votes: {len(TotalVotes)}\n")
output.write("-----------------------\n")
output.write(f'{Canidates[0]}: {percentagevotes[0]}% ({CanidateVotes[0]}) \n')
output.write(f'{Canidates[1]}: {percentagevotes[1]}% ({CanidateVotes[1]}) \n')
output.write(f'{Canidates[2]}: {percentagevotes[2]}% ({CanidateVotes[2]}) \n')
output.write(f'{Canidates[3]}: {percentagevotes[3]}% ({CanidateVotes[3]}) \n')
output.write("-----------------------\n")
output.write(f"Winner: {Winner}\n")
output.write("-----------------------")