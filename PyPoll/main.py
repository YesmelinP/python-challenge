#importing necessary libraries

import os 
import csv

#creating the file path to the csv election data 
csv_election_path =os.path.join("PyPoll","Resources","election_data.csv")

#inicializing variables to store election data 
candidates_votes = {}
vote_cast = 0
winner = {}

#opening and reading the election data CSV file
with open (csv_election_path) as csv_election:
    csvreader = csv.reader(csv_election, delimiter=",")

    #Read the header row 
    csv_header = next (csv_election)
    print(f"header: {csv_election}")

    #processing each row of election data 
    for row in csvreader:
        candidate = row[2]
        #counting votes for each candidate
        candidates_votes[candidate] = candidates_votes.get(candidate, 0) + 1
        #counting the total number of votes cast
        vote_cast = vote_cast + 1


#generating formatted results for each candidate 
candidate_formatted_results = []
for key in candidates_votes:
    votes = candidates_votes[key]
    #calculating the percentage of votes for each candidate 
    percentage = (votes / vote_cast) * 100
    formatted_percentage = "{:.3f}%".format(percentage)
    result = key + ": "+ formatted_percentage + " ("+str(votes)+")"
    candidate_formatted_results.append(result)
    
    #determining the winner based on the maximmum number of votes 
    if winner.get("value", 0) < votes:
        winner["name"] = key
        winner["value"] = votes

#sorting the candidate results alphabetically
candidate_formatted_results.sort()
#joining the candidate results into a single string with newlines
joined_candidates = "\n".join(candidate_formatted_results)

#constructiong the overall election results 

py_poll_result = f"""
Election Results
-------------------------
Total Votes {str(vote_cast)}
-------------------------
{joined_candidates}
-------------------------
Winner: {winner["name"]}
-------------------------
"""
#printing the election results to the console 
print(py_poll_result)

# Write PyPoll results to a text file
result_path = os.path.join("Pypoll","analysis", "Pypoll_result.txt")
with open(result_path, "w") as file:
    file.write(py_poll_result)