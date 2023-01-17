#Create and Read the file
import os
import csv

#Giving Path
FileOne = "C:\\Users\\surbh\\Downloads\\Gurpreet\\Gurpreet DA Study\\Python-Challenge\\PyPoll\\Resources\\election_data.csv"

with open(FileOne) as csvfile:

    # CSV reader & reading the first row 
    reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(reader)

    CandidateList = [Candidate[2] for Candidate in reader]
    
# Total Number of Votes
total_votes = len(CandidateList)

# List of Candidates with Count of Votes

Candidate_Details = [[Candidate,CandidateList.count(Candidate)] for Candidate in set(CandidateList)]

# Sorting the list using Key=Lambda function as used in PayBank
Candidate_Details = sorted(Candidate_Details, key=lambda x: x[1], reverse=True)

# Print
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for Candidate in Candidate_Details:
    percent_votes = (Candidate[1] / total_votes) * 100
    
    #Using 6.3f% to round of upto 6 decimals to 3 decimal points
    print(f'{Candidate[0]}: {percent_votes:6.3f}% ({Candidate[1]})')

print("-------------------------")
print(f"Winner: {Candidate_Details[0][0]}")
print("-------------------------")


#  Set the path & Enter details in txt file 

FileOne = "C:\\Users\\surbh\\Downloads\\Gurpreet\\Gurpreet DA Study\\Python-Challenge\\PyPoll\\Analysis\\Pypoll.txt"
with open(FileOne, "w") as text_file:
    print("Election Results", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print("-------------------------", file=text_file)

    for Candidate in Candidate_Details:
        percent_votes = (Candidate[1] / total_votes) * 100
        print(f'{Candidate[0]}: {percent_votes:6.3f}% ({Candidate[1]})', file=text_file)

    print("-------------------------", file=text_file)
    print(f"Winner: {Candidate_Details[0][0]}", file=text_file)
    print("-------------------------", file=text_file)

