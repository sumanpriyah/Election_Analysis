# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
# Import the datetime class from the datetime module.
import os
import csv

# print(f"initial cwd: {os.getcwd()}")
os.chdir(os.path.dirname(os.path.realpath(__file__)))
# print(f"final cwd: {os.getcwd()}")
#dir(csv)
# Assign a variable for the file to load and the path.
file_to_load =os.path.join("Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save= os.path.join("analysis", "election_analysis.txt")

# The general format for opening a file is
#election_data = open(file_to_load, 'r')

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options =[]
winning_candidate =""
winning_count = 0
winning_percentage = 0

#1. declare the empty disctonary 
candidate_votes={}

# Print the candidate name from each row

# Open the election results and read the file.
with open(file_to_load) as election_data:

   # To do :Perform analysis
   # print(election_data)

   # To do: read and analyze the data here.
   # Read the file object with the reader function.
   file_reader = csv.reader(election_data)
   
   
   # Read and print the header row.
   headers = next(file_reader)
   print(headers)
   
   # Print each row in the CSV file.
   for row in file_reader:
      total_votes = total_votes+1
   
      #print(total_votes) 
      
      candidate_name = row[2]
   
      # If the candidate does not match any existing candidate...
      if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]= 0
         # Add a vote to that candidate's count.
      candidate_votes[candidate_name] += 1
      
   with open(file_to_save, "w") as txt_file:
   # Print the final vote count to the terminal.
      election_results = (
         f"\nElection Results\n"
         f"-------------------------\n"
         f"Total Votes: {total_votes:,}\n"
         f"-------------------------\n")
      print(election_results, end="")
      # Save the final vote count to the text file.
      txt_file.write(election_results)
         

      # Determine the percentage of votes for each candidate by looping through the counts.
      # 1. Iterate through the candidate list.
      for candidate_name in candidate_votes:
         # 2. Retrieve vote count of a candidate.
         votes = candidate_votes[candidate_name]
         # 3. Calculate the percentage of votes.
         vote_percentage = float(votes) / float(total_votes) * 100
         # 4. Print the candidate name and percentage of votes.
         # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
         candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
         # Print each candidate, their voter count, and percentage to the terminal.
         print(candidate_results)
         #  Save the candidate results to our text file.
         txt_file.write(candidate_results)  
            
   if (votes > winning_count) and (vote_percentage>winning_percentage):     
      winning_count = votes 
      winning_percentage = vote_percentage
      winning_candidate= candidate_name

winning_candidate_summary = (
   f"-------------------------\n"
   f"Winner: {winning_candidate}\n"
   f"Winning Vote Count: {winning_count:,}\n"
   f"Winning Percentage: {winning_percentage:.1f}%\n"
   f"-------------------------\n")
      
   