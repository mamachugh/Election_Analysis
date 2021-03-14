import csv
import os

## Assign variable to load a file from a path.
csvpath = os.path.join("Resources", "election_results.csv")
## Assign variable to save a file to a path.
txtpath = os.path.join("analysis", "election_results.txt")

## Initialize a vote counter
total_votes = 0

## Create a list to contain all candidates
candidate_options = []

## Create a dictionary for votes by candidate
candidate_votes = {}

## Winning candidate, vote count, percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

## Open the election results file and read.
with open(csvpath) as csvfile: 
    reader = csv.reader(csvfile)
    
    ## Read the header row
    headers = next(reader)
    
    ## Print each row from the CSV file
    for row in reader:
        ## Add to the total vote count
        total_votes += 1
        
        ## Print the candidate name from each row
        candidate_name = row[2]
        
        ## If the candidate is not already in the list
        if candidate_name not in candidate_options: 
            
            ## Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            ## Create key (candidate_name) in dictionary
            candidate_votes[candidate_name] = 0

        ## Count the candidates' votes
        candidate_votes[candidate_name] +=1

with open(txtpath,"w") as txt_file: 
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    ## Loop to determine each candidates percentage of the vote
    ## Iterate thru the candidate_name list
    for candidate_name in candidate_votes:

        ## Bring back total vote count and percentage for each candidate
        votes = candidate_votes[candidate_name] 
        vote_percentage = float(votes)/float(total_votes) * 100

        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        ## Determine winning vote count, percentage, candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
