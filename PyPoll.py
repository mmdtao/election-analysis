#The data we need to retrieve
import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Initialize a list of candidate options
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
#election_data = open(file_to_load, "r")
with open(file_to_load) as election_data:
    
    # To do: read and analyze the data here.
    #print(election_data)
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)


    # Read the header row in the CSV file.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        #print(row)

        # 2. Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match an existing candidate...
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking the candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------\n")
    print(election_results, end="")

    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    
# Determine the percentage of votes for each candidate by looping through the counts.

    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        # 3. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)

        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):

           # If true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage

            # And set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

        # To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n")
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)
        
        # Print candidate results in text file.
        #candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        

       

    # 4. Print the candidate name and percentage of votes.
    #print(f"{candidate_name}: received {vote_percentage}% of the vote.")


        
    

# 3. Print the total cotes.
#print(total_votes)

# Print candidate list.
#print(candidate_options)

# Print candidate vote dictionary.
#print(candidate_votes)


# Close the file.
#election_data.close()



# Use the open statement to open the file as a text file
#outfile = open(file_to_save, "w")
# Using the with statement open the file as a text file
#with open(file_to_save, "w") as txt_file:

    # Write three counties to the file
    #txt_file("Hello World")
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")
    # or txt_file.write("Arapahoe, Denver, Jefferson")
    #txt_file.write("Counties in the Election\n-----------------\nArapahoe\nDenver\nJefferson")
# Write some data to the file.
#outfile.write("Hello World")

#Close the file
#outfile.close()

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of tbe election based on popular vote.


#Figure out what is wrong with retrieving csv file