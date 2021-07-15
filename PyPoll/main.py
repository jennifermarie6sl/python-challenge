import os
import csv

election_data_csv = os.path.join("python-challenge", "PyPoll", "Resources", "election_data.csv")
analysis_file = os.path.join("PyPoll", "Analysis", "Analysis.txt")

#CSV file management
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file)
    
    #Read/skip the header
#    csv_header = next(csv_file)
#    print (f'Header: {csv_header}')
    
    #extract first row to avoid appending to total
#    first_row = next(csv_reader) 