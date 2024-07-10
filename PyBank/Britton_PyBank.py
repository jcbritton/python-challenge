import os
import csv

# Read the CSV file into a DataFrame
with open("Resources/budget_data.csv", "r") as file:
    pybank = csv.reader(file)
    next(pybank)  # Skip the header row
    pybank_csv = list(pybank)

# Calculate the total number of months included in the dataset
Total_Months = len(pybank_csv)

# Convert the "Profit/Losses" column to integers
net_total = 0
changes = []
previous_row_value = None

for row in pybank_csv:
    row[1] = int(row[1])
    net_total += row[1]

    if previous_row_value is not None:
        change = row[1] - previous_row_value
        changes.append(change)
    previous_row_value = row[1]
# Calculate the net total amount of "Profit/Losses" over the entire period
Total = f"${net_total}"

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
if len(changes) == 0:
    average_change = 0
else: 
    average_change = f"${sum(changes) / len(changes):.2f}"

#The greatest increase in profits (date and amount) over the entire period
greatest_increase = changes[0]
index_greatest_increase = 1
greatest_decrease = changes[0]
index_greatest_decrease = 1

for index, change in enumerate(changes):
    if change > greatest_increase:
        greatest_increase = change
        index_greatest_increase = index
    elif change < greatest_decrease:
        greatest_decrease = change
        index_greatest_decrease = index   

date_greatest_increase = pybank_csv[index_greatest_increase + 1][0]
date_greatest_decrease = pybank_csv[index_greatest_decrease + 1][0]

# The greatest decrease in losses (date and amount) over the entire period
for j in changes:    
    if all(j < change for change in changes): 
        greatest_decrease = j
        date_greatest_decrease = pybank_csv[j][0]

# Find the index of the row with the greatest increase in "Profit/Losses"
index_greatest_increase = changes.index(max(changes))

# Find the index of the row with the greatest decrease in "Profit/Losses"
index_greatest_decrease = changes.index(min(changes))

# Print the analysis to the terminal
print("Financial Analysis\n \n---------------------------------\n \n"
      f"Total Months: {Total_Months}\n"
      f"Total: {Total}\n"
      f"Average Change: {average_change}\n"
      f"Greatest Increase: {date_greatest_increase} (${greatest_increase})\n"
      f"Greatest Decrease: {date_greatest_decrease} (${greatest_decrease})")

# Export the analysis to a text file
output_file = os.path.join("C:\\Users\\Owner\\Desktop\\python-challenge\\PyBank\\Analysis", "financial_analysis.txt")
with open(output_file, "w") as file:
    file.write("Financial Analysis\n \n---------------------------------\n \n"
               f"Total Months: {Total_Months}\n"
               f"Total: {Total}\n"
               f"Average Change: {average_change}\n"
               f"Greatest Increase: {date_greatest_increase} (${greatest_increase})\n"
               f"Greatest Decrease: {date_greatest_decrease} (${greatest_decrease})")