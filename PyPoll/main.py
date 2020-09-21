import csv
import os

#set path to the election_data.csv which is in the resources folder
#csvpath = os.path.join("Resources","election_data.csv")
election_data_path = "Resources/election_data.csv"

#in the csv file
with open(election_data_path) as electionfileStream:   

    #make a list of the candidates
    candidates = []
    candidates_votecount = []

    electioncsvreader = csv.reader(electionfileStream, delimiter = ",")

    #skip the header row
    electioncsv_header = next(electioncsvreader)
    
    #for each row
    for row in electioncsvreader:

        #check if candidate is added to the candidates list
        if row[2] in candidates:
            #add a vote for the candidate
            candidate_index = candidates.index(row[2])
            candidates_votecount[candidate_index] = candidates_votecount[candidate_index] + 1
        else:
            #add the candidate to the candidate list and to the candidate_votecount list with one vote
            candidates.append(row[2])
            candidates_votecount.append(1)

    #calculate total number of votes
    total_votes = sum(candidates_votecount)
    
    #find the candidate index with the most votes
    max_votes = max(candidates_votecount)
    winner_index = candidates_votecount.index(max_votes)

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    
    for name in candidates:
        #find percentage of votes each candidate won
        votes = candidates_votecount[candidates.index(name)]/total_votes
        vote_percent = "{:.3%}".format(votes)
        print(f"{name}: {vote_percent} ({candidates_votecount[candidates.index(name)]})")
   
    print("-------------------------")
    print(f"Winner: {candidates[winner_index]}")
    print("-------------------------")

