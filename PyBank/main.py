import os
import csv

budget_data_csv = os.path.join(".", "Resources", "budget_data.csv")
analysis_file = os.path.join("PyBank", "Analysis", "Analysis.txt")

#defining variables
#Month Variables
months = 0
months_changed = []
total_months = []
     
#Dollar Variables
p_l_start= 0
net_change_list = []
increase = [" ", " "]
decrease = []

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
        new_name= int(row[1]) - net_change
        net_change = int(row[1])
        p_l_start += net_change
        net_change_list = net_change_list + [new_name]
        months_changed = months_changed + [row[0]]
        
        increase = max(net_change_list)
        if row ==increase:
            increase[0] = row[0]
            increase[1] = net_change_list
        #print(increase)
        
        decrease = min(net_change_list)
        if row == decrease:
            decrease[0] = row[0]
            decrease[1] = net_change_list
        #print(net_change)

    #Calcs:
    average = sum(net_change_list)/ len(net_change_list)
    #print(round(average, 2))
  
    output = (f"\nFinancial Analysis\n"
        f"------------------------------------------------\n"
        f"Total Months: {months}\n"
        f"Total: ${p_l_start}\n"
        f"Average Change ${round(average, 2)}\n"
        f"Greatest Increase in Profits: (${increase})\n"
        f"Greatest Decrease in Profits: (${decrease})\n")

    print(output)
    print("what?")
    #bring date and $ for increase and decrease
    