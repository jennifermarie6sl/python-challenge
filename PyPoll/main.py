import os
import csv

election_data_csv = os.path.join(".", "PyPoll", "Resources", "election_data.csv")
analysis_file = os.path.join("PyPoll", "Analysis", "Analysis.txt")

#Define variables, lists and dictionaries
candidate_options = []
candidate_votes = {}
votes_count = []
total_votes = 0
    
#CSV file management
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file)
    
    #Read/skip the header
    csv_header = next(csv_file)
    
    for row in csv_reader:
        votes_count.append(row[0])
        candidate_name = row[2]
         
        total_votes = total_votes + 1
        
        if candidate_name not in candidate_options: 
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] =0 
        candidate_votes[candidate_name] += 1 
            
    #winner variables
    maxVotes = 0
    winner = "" #empty string
    
    for candidate, votes in candidate_votes.items():
        
        #calc winner
        if votes > maxVotes:
            maxVotes = votes
            winner = candidate
        
        #calc %
        if candidate == "Khan":
            Khan_votes = votes
            Khan_percent = round((votes / total_votes) * 100, 3)
        elif candidate == "Correy":
            Correy_votes = votes
            Correy_percent = round((votes / total_votes) * 100, 3)  
        elif candidate == "Li":
            Li_votes = votes
            Li_percent = round((votes / total_votes) * 100, 3)
        elif candidate == "O'Tooley":
            Tooley_votes = votes
            Tooley_percent = round((votes / total_votes) * 100, 3)  

output = (f"\nElection Results\n"
        f"------------------------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------------------------------\n"
        f"Khan: {Khan_percent:.3f}% ({Khan_votes:,}) \n"
        f"Correy: {Correy_percent:.3f}% ({Correy_votes:,})\n"
        f"Li: {Li_percent:.3f}% ({Li_votes:,})\n"
        f"O'Tooley: {Tooley_percent:.3f}% ({Tooley_votes:,})\n"
        f"------------------------------------------------\n"
        f"Winner: {winner}\n")
print(output)
    
with open(analysis_file ,"w") as txt_file:
    txt_file.write(output)