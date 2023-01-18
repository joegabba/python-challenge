#Get dependencies
import os
import csv


#Assign file location with the pathlib library
csv_file = os.path.join("..", "python-challenge", "recources", "election_data.csv")

#Variables 
total_votes = 0 
stockham_votes = 0
doane_votes = 0
degette_votes = 0


#Open csv in default read mode with context manager
with open(csv_file ,newline="", encoding="utf-8") as elections:

    #Store data under the csvreader variable
    csv_reader = csv.reader(elections, delimiter=",") 

    #Skip the header so we iterate through the actual values
    header = next(csv_reader)     

    #Iterate through each row in the csv
    for row in csv_reader: 

        # Count the unique Voter ID's and store in variable  called total_votes
        total_votes +=1
        
        # We have four candidates if the name is found, count the times it appears and store in a list
        # We can use this values in our percent vote calculation in the print statements
        if row[2] == "Charles Casper Stockham": 
            stockham_votes +=1
        elif row[2] == "Raymon Anthony Doane":
            doane_votes +=1
        elif row[2] == "Diana DeGette": 
            degette_votes +=1
        
    
    
 # To find the winner we want to make a dictionary out of the two lists we previously created 
candidates = ["Stockham", "Doane", "DeGette"]
votes = [stockham_votes, doane_votes, degette_votes]

# We zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)
print(f'-----test----{votes}')

# Print a the summary of the analysis
stockham_percent = (stockham_votes/total_votes) *100
doane_percent = (doane_votes/total_votes) * 100
degette_percent = (degette_votes/total_votes)* 100


# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Stockham: {stockham_percent:.3f}% ({stockham_votes})")
print(f"Doane: {doane_percent:.3f}% ({doane_votes})")
print(f"DeGette: {degette_percent:.3f}% ({degette_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# Output files
# Assign output file location and with the pathlib library
#output_file = Path("..", "pypoll", "Election_Results_Summary.txt")

with open("Election_Results_Summary.txt", "w") as file:

# Write methods to print to Elections_Results_Summary 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Stockham: {stockham_percent:.3f}% ({stockham_votes})")
    file.write("\n")
    file.write(f"Doane: {doane_percent:.3f}% ({doane_votes})")
    file.write("\n")
    file.write(f"DeGette: {degette_percent:.3f}% ({degette_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")

