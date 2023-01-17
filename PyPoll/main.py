import os
import csv

FileOne = "C:\\Users\\surbh\\Downloads\\Gurpreet\\Gurpreet DA Study\\Python-Challenge\\PyPoll\\Resources\\election_data.csv"

with open(FileOne) as csvfile:

    # CSV reader specifiing the delimiter and variable that holds contents within the file
    reader = csv.reader(csvfile, delimiter=',')

    # Reading the first row (header)
    csv_header = next(reader)

    CandidateList = [candidate[2] for candidate in reader]
    
# Calculating the number of total votes
total_votes = len(CandidateList)

# Creating a unique list of the candidates with the corresponding number of votes
canditates_info = [[candidate,CandidateList.count(candidate)] for candidate in set(CandidateList)]

# Sorting the list so that the first candidate becomes the winner 
canditates_info = sorted(canditates_info, key=lambda x: x[1], reverse=True)

# Printing the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in canditates_info:
    percent_votes = (candidate[1] / total_votes) * 100
    print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})')

print("-------------------------")
print(f"Winner: {canditates_info[0][0]}")
print("-------------------------")


#  Printing the  election results to text file 
# Set path for file
FileOne = "C:\\Users\\surbh\\Downloads\\Gurpreet\\Gurpreet DA Study\\Python-Challenge\\PyPoll\\Resources\\Pypoll.txt"
with open(FileOne, "w") as text_file:
    print("Election Results", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print("-------------------------", file=text_file)

    for candidate in canditates_info:
        percent_votes = (candidate[1] / total_votes) * 100
        print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})', file=text_file)

    print("-------------------------", file=text_file)
    print(f"Winner: {canditates_info[0][0]}", file=text_file)
    print("-------------------------", file=text_file)

