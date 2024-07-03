import pandas as pd
import os
import csv

# Read the CSV file into a DataFrame
pypoll_csv = pd.read_csv("C:\\Users\\Owner\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.csv")

# Calculate the total number of votes cast
Total_votes = len(pypoll_csv)

# List the candidates who received votes
Candidates = pypoll_csv["Candidate"].unique()

# Calculate the total number of votes each candidate won
Votes = pypoll_csv["Candidate"].value_counts()

# Calculate the percentage of votes each candidate won
Percentage = Votes / Total_votes

# Determine the winner of the election based on popular vote
Winner = Votes.idxmax()

# Print the analysis to the terminal
print("Election Results\n \n-------------------------\n \n"
      f"Total Votes: {Total_votes}\n"
      "-------------------------\n")
for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {Percentage[i]:.3%} ({Votes[i]})")
print("-------------------------")
print(f"Winner: {Winner}")
print("-------------------------")

# Export the analysis to a text file
output_file = os.path.join("C:\\Users\\Owner\\Desktop\\python-challenge\\PyPoll\\Analysis", "election_analysis.txt")
with open(output_file, "w") as file:
    file.write("Election Results\n \n-------------------------\n \n"
               f"Total Votes: {Total_votes}\n \n"
               "-------------------------\n \n")
    for i in range(len(Candidates)):
        file.write(f"{Candidates[i]}: {Percentage[i]:.3%} ({Votes[i]})\n \n")
    file.write("-------------------------\n \n")
    file.write(f"Winner: {Winner}\n \n")
    file.write("-------------------------")