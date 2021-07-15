import os
import csv

election_data_csv = os.path.join(".", "election_data.csv")
analysis_file = os.path.join("PyPoll", "Analysis", "Analysis.txt")

#CSV file management
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file)
    
    #Read/skip the header
    csv_header = next(csv_file)
    print (f'Header: {csv_header}')
    
    #extract first row to avoid appending to total
    first_row = next(csv_reader) 
    print(first_row)
    
    #Define variable
    candidate_options = []
    candidate_votes = {}
    votes_count = []
    
    for row in csv_reader:
    #    print(row) #tester row
    
        #candidate_name = row(2)
        votes_count.append(row[0])
    #print(votes_count)    
    #print(len(votes_count))
    #print(candidate_name)
    
    output = (f"\nElection Results\n"
        f"------------------------------------------------\n"
        f"Total Votes: {len(votes_count)}\n"
        f"------------------------------------------------\n"
        f"\n"
        f"\n"
        f"\n"
        f"\n"
        f"------------------------------------------------\n"
        f"Winner:\n")
    print(output)