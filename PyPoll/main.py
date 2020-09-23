import csv
import os

#set path to the election_data.csv which is in the resources folder
election_data_path = os.path.join("Resources","election_data.csv")

#open the csv file to read
with open(election_data_path) as electionfileStream:   

    #create a dictionary to contain candidates and their votecount
    candidates = {}

    electioncsvreader = csv.reader(electionfileStream, delimiter = ",")

    #skip the header row
    electioncsv_header = next(electioncsvreader)
    
    #for each row
    for row in electioncsvreader:

        #check if candidate is added to the candidates dictionary
        if row[2] in candidates:
            #add a vote for the candidate
            candidates[row[2]] = candidates[row[2]] + 1

        else:
            #add the candidate to the dictionary with one vote
            candidates[row[2]] = 1

    #calculate total number of votes
    total_votes = sum(candidates.values())
    
    #find the maximum votes
    max_votes = max(candidates.values())

    #create a list to print the election results
    line = ["Election Results"]
    line.append("-------------------------")
    line.append("Total Votes: " + str(total_votes))
    line.append("-------------------------")
    
    for name in candidates:
        #find percentage of votes each candidate won
        vote_percent = round((candidates[name]/total_votes)*100,2)
        line.append(name + ": " + str(vote_percent) + "% " + str(candidates[name]))
        #find the winner
        if max_votes == candidates[name]:
            winner = name
   
    line.append("-------------------------")
    line.append("Winner: " + winner)
    line.append("-------------------------")

    print("\n".join(line))

    #export the election results to a text file
    output_path = os.path.join("Analysis","Election_Results.txt")

    with open(output_path,"w") as resultsfile:

        #write the election results to the file
        resultsfile.writelines("\n".join(line))

