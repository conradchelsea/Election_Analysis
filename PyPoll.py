#For this project:
#Gather the total # of votes cast.
#Create a list of candidates who received votes.
#Collect the total number of votes each candidate received. 
#Get the percentage of votes each candidate won. 
#Determine the winner based on the popular vote. 

# Import the datetime class from the datetime module.
#import datetime
# Use the now() attribute on the datetime class to get the present time.
#now = datetime.datetime.now()
# Print the present time.

#Assign a variable for the file to load and a path. 
#file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file
#with open(file_to_load) as election_data:

     # To do: perform analysis.
     #print(election_data)

#import csv
#import os
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
     #print(election_data)

     #print("The time right now is ", now)
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")


# Close the file
#outfile.close()
# Write three counties to the file.
     #txt_file.write("Arapahoe, ")
     #txt_file.write("Denver, ")
     #txt_file.write("Jefferson")

  # Add our dependencies.
#import csv
#import os
# Assign a variable to load a file from a path.
#file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
#with open(file_to_load) as election_data:#
    #file_reader = csv.reader(election_data)

    # Read and print the header row.
    #headers = next(file_reader)
    #print(headers)   
# Add our dependencies.
#import csv
#import os
# Assign a variable to load a file from a path.
#file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
#with open(file_to_load) as election_data:
    #file_reader = csv.reader(election_data)

    # Read the header row.
    #headers = next(file_reader)

    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

# 3. Print the total votes.
print(total_votes)

        # Candidate Options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        candidate_options.append(candidate_name)

# Print the candidate list.
print(candidate_options)

# Print each row in the CSV file.
for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
 
        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

# Print the candidate list.
print(candidate_options)
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data: