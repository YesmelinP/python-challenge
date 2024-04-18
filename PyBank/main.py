#importing resources 

import os 
import csv

#File path to the CSV budget data
csv_budget_path = os.path.join('PyBank','Resources', 'budget_data.csv')

# Open and read the CSV file
with open (csv_budget_path) as csv_budget:
    csv_reader = csv.reader(csv_budget, delimiter=",")

    #Read the header row
    csv_header = next (csv_budget)
    print(f"Header: {csv_header}")

    #Initialize variables to store analysis results
    date = []
    net_total_amount = 0
    months = [] #list to store each month's data 
    greates_increase = {} #value, month
    greates_decrease = {} #value, month

    # Loop through each row of data after the header
    for row in csv_reader:
        # Extract date and profit/losses for each month
        record = {"Date": (row[0]),"Profit/Losses": int(row[1])}
        months.append(record)
        # Calculate the net total amount
        net_total_amount += record["Profit/Losses"]
    
    # Calculate the change in profit/losses between each month
    change = [] # List to store changes in profit/losses
    for index, month in enumerate(months):
       if index < len(months) - 1:
        difference = months[index + 1]["Profit/Losses"] - month["Profit/Losses"]
        change.append(difference)
        # Update greatest increase and decrease if applicable
        if  greates_increase.get("value", 0) < difference:
           greates_increase["value"] = difference
           greates_increase["month"] = months[index + 1]["Date"]
        if  greates_decrease.get("value", 0) > difference:
           greates_decrease["value"] = difference
           greates_decrease["month"] = months[index + 1]["Date"]
       
sorted_change = sorted(change)    

#1.Calculate the total number of months 
total_months = len(months)
average_change = sum(change)/len(change)

#2.calculating the total net in the loop print
print("Total: $",str(net_total_amount))

#3.Calculating the average change
print(f"Average change: {(average_change)}")

#3/4. Calculating Greatest Increase in Profits
greatest_increase_profits = f"{greates_increase['month']} ({greates_increase['value']})"
greatest_decrease_profits = f"{greates_decrease['month']} ({greates_decrease['value']})"


#constructiong the overall election results 

py_bank_result = f"""
Financial Analysis
----------------------------
Total Months: {str(total_months)}
Total: {str(net_total_amount)}
Average Change: {str(average_change)}
Greatest Increase in Profits: {str(greatest_increase_profits)}
Greatest Decrease in Profits: {str(greatest_decrease_profits)}
"""

#printing the bank results to the console 
print(py_bank_result)

# Write bank results to a text file
result_path = os.path.join("PyBank","analysis", "PyBank_result.txt")
with open(result_path, "w") as file:
    file.write(py_bank_result)