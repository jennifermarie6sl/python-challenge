import os
import csv

budget_data_csv = os.path.join(".", "PyBank", "Resources", "budget_data.csv")
analysis_file = os.path.join("PyBank", "Analysis", "Analysis.txt")

#defining variables
#Month Variables
months = 0
months_changed = []
change_list = []
     
#Dollar Variables
#profit_loss_values = int(budget_data[1])
#months_total = sum(months)

#CSV file management
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")
    
    #Read the header
    csv_header = next(csv_file)
    print (f'Header: {csv_header}')
        
#    print sum(profit_loss)
    
profit_loss = []
#for data in csv_reader:
#            profit_loss.append(float(data[2])
            
#        data_dictionary = {}
#        data_dictionary["dollars"] = profit_loss
#        data_dictionary["sum"] = sum(data_dictionary["dollars"])
#        print(data_dictionary)

       
    
    
    
                              
#    print(for fiber in data_dictionary["fiber"]:
#            print (fiber)
#          print(sum(data_dictionary["fiber"])