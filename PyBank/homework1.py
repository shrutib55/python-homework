import csv
from pathlib import Path
csv_file = Path('budget_data.csv')
total_months = 0
month_of_change = []
net_change_list = []
top_increase = ["", 0]
top_decrease = ["", 9999999999999]
total_net = 0
with open(csv_file) as financial_data:
    reader = csv.reader(financial_data)
    
    header = next(reader)
    
    first_row = next(reader)
    
    total_months = total_months + 1
    
    total_net = total_net + int(first_row[1])
    
    prev_net = int(first_row[1])
    
    for row in reader:
        
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list.append(net_change)
        month_of_change.append(row[0])
        
        if net_change > top_increase[1]:
            top_increase[0] = row[0]
            top_increase[1] = net_change
            
        if net_change < top_decrease[1]:
            top_decrease[0] = row[0]
            top_decrease[1] = net_change
monthly_average = sum(net_change_list)/len(net_change_list) 
monthly_average
output_file = Path('budget_analysis.txt')
with open(output_file, "w") as txt_file:
    txt_file.write(f"Finanial Analysis\n")
    txt_file.write("------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Average Change: {monthly_average}\n")
    txt_file.write(f"Greatest Increase in Profits: {top_increase[0]}, {top_increase[1]}\n")
    txt_file.write(f"Greatest Decrease in Profits: {top_decrease[0]}, {top_decrease[1]}\n")