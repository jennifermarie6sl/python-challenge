import os
import csv

budget_data_csv = os.path.join(".", "PyBank" ,"Resources", "budget_data.csv")
analysis_file = os.path.join("PyBank", "Analysis", "Analysis.txt")

#defining variables:
#Month Variables
months = 0
months_changed = []
total_months = []
     
#Dollar Variables
p_l_start= 0
net_change_list = []

#Max Variable
max_increase = 0
max_decrease = 0
max_increase_month = " "
max_decrease_month = " "

#CSV file management
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file)
    
    #Read/skip the header
    csv_header = next(csv_file)
       
    #extract first row to avoid appending to total
    first_row = next(csv_reader) 
        
    #Place holders for starting points for "for loop"
    months = months + 1 #takes starting months value of 0 and adds 1
    p_l_start += int(first_row[1])
    net_change= int(first_row[1])
        
    for row in csv_reader:
        
        #Track new changes
        months = months + 1
        delta= int(row[1]) - net_change
        net_change = int(row[1])
        p_l_start += (net_change)
        net_change_list = net_change_list + [delta]
        months_changed = months_changed + [row[0]]
        
        if net_change > max_increase:
            max_increase = net_change
            max_increase_month = row[0]
        
        if delta < max_decrease:
            max_decrease = delta
            max_decrease_month = row[0]   

    #Calcs:
    average = sum(net_change_list)/ len(net_change_list)
        
    output = (f"\nFinancial Analysis\n"
        f"------------------------------------------------------\n"
        f"Total Months: {months}\n"
        f"Total: ${p_l_start:,}\n"
        f"Average Change ${round(average, 2):,}\n"
        f"Greatest Increase in Profits: {max_increase_month} (${max_increase:,})\n"
        f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease:,})\n")

    print(output)

with open(analysis_file ,"w") as txt_file:   
    txt_file.write(output)