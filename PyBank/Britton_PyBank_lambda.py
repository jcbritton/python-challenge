import os
import csv

# Read the CSV file into a DataFrame
with open("C:\\Users\\Owner\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv", "r") as file:
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
    
# Calculate changes and store them with the corresponding dates
changes = []
for i in range(1, len(pybank_csv)):
    change = int(pybank_csv[i][1]) - int(pybank_csv[i-1][1])
    changes.append((pybank_csv[i][0], change))  # Store date and change as a tuple

# Find the greatest increase and decrease
greatest_increase = max(changes, key=lambda x: x[1])
greatest_decrease = min(changes, key=lambda x: x[1])

# Print the analysis to the terminal
print("Financial Analysis\n \n---------------------------------\n \n"
      f"Total Months: {Total_Months}\n"
      f"Total: {Total}\n"
      f"Average Change: {average_change}\n"
      f"Greatest Increase: {greatest_increase[0]} (${greatest_increase[1]})\n"
      f"Greatest Decrease: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Export the analysis to a text file
output_file = os.path.join("C:\\Users\\Owner\\Desktop\\python-challenge\\PyBank\\Analysis", "financial_analysis.txt")
with open(output_file, "w") as file:
    file.write("Financial Analysis\n \n---------------------------------\n \n"
               f"Total Months: {Total_Months}\n"
               f"Total: {Total}\n"
               f"Average Change: {average_change}\n"
               f"Greatest Increase: {greatest_increase[0]} (${greatest_increase[1]})\n"
               f"Greatest Decrease: {greatest_decrease[0]} (${greatest_decrease[1]})")