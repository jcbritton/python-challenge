import pandas as pd
import os
import csv

# Read the CSV file into a DataFrame
pybank_csv = pd.read_csv("C:\\Users\\Owner\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv")

# Calculate the total number of months included in the dataset
Total_Months = len(pybank_csv)

# Calculate the net total amount of "Profit/Losses" over the entire period
Total = f"${pybank_csv['Profit/Losses'].sum():.0f}"

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
average_change = f"${pybank_csv['Profit/Losses'].diff().mean():.2f}"

# The greatest increase in profits (date and amount) over the entire period
greatest_increase = f"${pybank_csv['Profit/Losses'].diff().max():.0f}"

# The greatest decrease in losses (date and amount) over the entire period
greatest_decrease = f"${pybank_csv['Profit/Losses'].diff().min():.0f}"

# Find the index of the row with the greatest increase in "Profit/Losses"
index_greatest_increase = pybank_csv['Profit/Losses'].diff().idxmax()

# Find the index of the row with the greatest decrease in "Profit/Losses"
index_greatest_decrease = pybank_csv['Profit/Losses'].diff().idxmin()

# Use this index to find the corresponding date
date_greatest_increase = pybank_csv.loc[index_greatest_increase, 'Date']

# Use this index to find the corresponding date
date_greatest_decrease = pybank_csv.loc[index_greatest_decrease, 'Date']

# Print the analysis to the terminal
print("Financial Analysis\n \n---------------------------------\n \n"
      f"Total Months: {Total_Months}\n"
      f"Total: {Total}\n"
      f"Average Change: {average_change}\n"
      f"Greatest Increase: {date_greatest_increase} ({greatest_increase})\n"
      f"Greatest Decrease: {date_greatest_decrease} ({greatest_decrease})")

# Export the analysis to a text file
output_file = os.path.join("C:\\Users\\Owner\\Desktop\\python-challenge\\PyBank\\Analysis", "financial_analysis.txt")
with open(output_file, "w") as file:
    file.write("Financial Analysis\n \n---------------------------------\n \n"
               f"Total Months: {Total_Months}\n"
               f"Total: {Total}\n"
               f"Average Change: {average_change}\n"
               f"Greatest Increase: {date_greatest_increase} ({greatest_increase})\n"
               f"Greatest Decrease: {date_greatest_decrease} ({greatest_decrease})")
    