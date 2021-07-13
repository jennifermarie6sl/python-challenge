import os
import csv

budget_data_csv = os.path.join(".", "PyBank", "Resources", "budget_data.csv")
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
    #print (f'Header: {csv_header}')
    
    #extract first row to avoid appending to total
    first_row = next(csv_reader) 
    #print(first_row) #tester to see if it returns value in first row
    months = months + 1 #takes starting months value of 0 and adds 1
    #print(months)
    p_l_start = p_l_start + int(first_row[1])
    #print(p_l_start)
    net_change= int(first_row[1])
    #print(net_change)
    
    for row in csv_reader:
        
        #Start tracking
        months = months + 1
        #print(months)#prints list of count of months
        p_l_start = p_l_start + int(first_row[1])
        #print(p_l_start)
        
        #Track new changes
        new_name= int(row[1]) - net_change
        net_change = int(row[1])
        net_change_list = net_change_list + [new_name]
        months_changed = months_changed + [row[0]]
        #print(months_changed)
        #print(net_change_list)
        

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
    #print(p_l_start)
    print(p_l_start)

        
    output = (f"\nFinancial Analysis\n"
        f"------------------------------------------------\n"
        f"Total Months: {months}\n"
        #    f"Total: ${}\n"
        f"Average Change ${round(average, 2)}\n"
        f"Greatest Increase in Profits: (${increase})\n"
        f"Greatest Decrease in Profits: (${decrease})\n")

    print(output)
    #Total not working
    #bring date and $ for increase and decrease