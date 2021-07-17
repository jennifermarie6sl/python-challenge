import os
import csv

election_data_csv = os.path.join(".", "PyPoll" ,"Resources", "election_data.csv")
analysis_file = os.path.join("PyPoll", "Analysis", "Analysis.txt")

#CSV file management
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file)
    
    #Read/skip the header
    csv_header = next(csv_file)
        
    #extract first row to avoid appending to total
    first_row = next(csv_reader) 
        
    #Define variables, lists and dictionaries
    candidate_options = []
    candidate_votes = {} # here
    votes_count = []
    total_votes = 0
    
    for row in csv_reader:
        votes_count.append(row[0])
        
        candidate_name = row[2]
        
        total_votes = total_votes + 1
        
        if candidate_name not in candidate_options: 
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] =0  #here
        candidate_votes[candidate_name] += 1  #here
    #print(candidate_options[0])
    #print(candidate_votes)
    #print(total_votes)
    
    #winner based on popular votes
    maxVotes = 0
    winner = "" #empty string
    
    for candidate, votes in candidate_votes.items():
        if votes > maxVotes:
            maxVotes = votes
            winner = candidate
        
        if candidate == "Khan":
            Khan_votes = votes
            Khan_percent = round((votes / total_votes) * 100, 3)
        elif candidate == "Correy":
            Correy_votes = votes
            Correy_percent = round((votes / total_votes) * 100, 3)  
        elif candidate == "Khan":
            Khan_votes = votes
            Khan_percent = round((votes / total_votes) * 100, 3)
        elif candidate == "Correy":
            Correy_votes = votes
            Correy_percent = round((votes / total_votes) * 100, 3)  
        #calc %
    
    #winner = max(candidate_votes.values())
    #print(winner) 
    print(Khan_percent)
    print(candidate_votes["Khan"])
    
    