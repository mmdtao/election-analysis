#The data we need to retrieve
import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Open the election results and read the file.
#election_data = open(file_to_load, "r")
with open(file_to_load) as election_data:
    
    # To do: read and analyze the data here.
    #print(election_data)
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)


    # Read and print the header row in the CSV file.
    headers = next(file_reader)
    print(headers)

# Close the file.
election_data.close()



# Use the open statement to open the file as a text file
#outfile = open(file_to_save, "w")
# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file
    #txt_file("Hello World")
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")
    # or txt_file.write("Arapahoe, Denver, Jefferson")
    txt_file.write("Counties in the Election\n-----------------\nArapahoe\nDenver\nJefferson")
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