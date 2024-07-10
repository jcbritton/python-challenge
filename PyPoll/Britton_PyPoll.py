import csv
import os

# Read the CSV file
with open("C:\\Users\\Owner\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    data = list(reader)

# Calculate the total number of votes cast
Total_votes = len(data)

# Create a dictionary to store the number of votes for each candidate
Votes = {}

# Count the votes for each candidate
for row in data:
    candidate = row[2]
    if candidate in Votes:
        Votes[candidate] += 1
    else:
        Votes[candidate] = 1

# Calculate the percentage of votes each candidate won
Percentage = {candidate: votes / Total_votes for candidate, votes in Votes.items()}

# Determine the winner of the election based on popular vote
Winner = max(Votes, key=Votes.get)

# Print the analysis to the terminal
print("Election Results\n \n-------------------------\n \n"
      f"Total Votes: {Total_votes}\n \n"
      "-------------------------\n \n")
for candidate, votes in Votes.items():
    print(f"{candidate}: {Percentage[candidate]:.3%} ({votes})\n \n")
print("-------------------------\n \n")
print(f"Winner: {Winner}\n \n")
print("-------------------------")

# Export the analysis to a text file
output_file = os.path.join("C:\\Users\\Owner\\Desktop\\python-challenge\\PyPoll\\Analysis", "election_analysis.txt")
with open(output_file, "w") as file:
    file.write("Election Results\n \n-------------------------\n \n"
               f"Total Votes: {Total_votes}\n \n"
               "-------------------------\n \n")
    for candidate, votes in Votes.items():
        file.write(f"{candidate}: {Percentage[candidate]:.3%} ({votes})\n \n")
    file.write("-------------------------\n \n")
    file.write(f"Winner: {Winner}\n \n")
    file.write("-------------------------")