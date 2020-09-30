import os
import csv

analysis_csv = os.path.join("Resources", "election_data.csv")
results_txt = os.path.join("Analysis", "results.txt")

# Lists to store data

candidates = []
# creating a dictonary
candidates_votes = {}
total_votes=0
percent = []


with open(analysis_csv) as cvsfile:
    csvreader = csv.reader(cvsfile, delimiter=",")

    header = next(csvreader)

    for row in csvreader:
        candidates= row[2]
        #create a list to calculate the votes 
        if candidates in candidates_votes.keys():
            candidates_votes[candidates]=candidates_votes[candidates]+1
        else:
            candidates_votes[candidates]=1
#writing to a file
with open(results_txt, "w") as textfile:
    #displaying total votes
    total_votes=sum(candidates_votes.values())
    result =  f"total Votes {total_votes}\n"
    textfile.write(result)
    print (result)
    for i in candidates_votes:
        #calculating percentage and rounding the number
        percent = round((candidates_votes[i]/total_votes)*100, 0)
        result = f"{i} {percent}% {candidates_votes[i]}\n"
        textfile.write(result)
        print (result)

    for key in candidates_votes.keys():
        #using max function to display the winner
        if candidates_votes[key]==max(candidates_votes.values()):
            winner = key

    result = f"Winner is {winner}"
    textfile.write(result)
    print(result)

