This homework assignment was completed with the help of ([Perplexity AI](https://www.perplexity.ai/search/given-the-following-code-snipp-_sWxdKtnQPmahUHE3QAmgw)).

# Perplexity AI Conversation - Lambda Solution
>Given the following code snippet, why is the output for date_greatest_increase one month off? It should say:
```
Greatest Increase: Aug-16 ($1862002)
Greatest Decrease: Feb-14 ($-1825558)
```
>but instead outputs:
                         
```
Greatest Increase: Jul-16 ($1862002)
GreatestDecrease: Jan-14 ($-1825558)
```    
                                                                         
```
import os
import csv

Read the CSV file into a DataFrame
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

date_greatest_increase = pybank_csv[index_greatest_increase][0]
date_greatest_decrease = pybank_csv[index_greatest_decrease][0]

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
               f"Greatest Increase: {date_greatest_increase} ({greatest_increase})\n"
               f"Greatest Decrease: {date_greatest_decrease} ({greatest_decrease})")
```
# Answer
The issue in your code is related to how you're calculating and associating the changes with the dates. The changes are calculated between consecutive months, but you're associating them with the dates of the current month instead of the next month. Here's why:
When you calculate the changes, you're doing it like this:
change = current_month_value - previous_month_value
But you're associating this change with the current month's date, when it actually represents the change from the previous month to the current month.
To fix this, you need to shift the dates by one month when reporting the greatest increase and decrease. Here's how you can modify your code:
```
python
# ... (previous code remains the same)

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

# ... (rest of the code remains the same)
```

In this modified version:
We calculate the changes and store them as tuples along with their corresponding dates.
We use the max() and min() functions with a key parameter to find the greatest increase and decrease, which will correctly associate the changes with their dates.
This should correct the issue and give you the expected output:
```
Greatest Increase: Aug-16 ($1862002)
Greatest Decrease: Feb-14 ($-1825558)
```

The key is to remember that each change represents the difference from the previous month to the current month, so it should be associated with the current month's date.
