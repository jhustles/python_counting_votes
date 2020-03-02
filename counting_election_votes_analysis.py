#!/usr/bin/env python
# coding: utf-8

# # Counting Election Votes
# 

# In[1]:


# Import Dependencies
import os
import csv


# In[2]:


# Set the File Path
filepath = os.path.join(".","resources","election_data.csv")
output_file = os.path.join(".", "votes.txt")


# In[3]:


with open (filepath, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    # create buckets
    votes_list = []
    votes_dict = {}
    
    # Loop 1 - Collect all votes of candidates name in a long list
    for row in csvreader:
        votes_list.append(row[2])
    total_votes = len(votes_list)
    # Loop 2 - for each name in the votes list, if the candidate doesn't exist in the dictionary, create one for
    # that person and set to zero, and add 1 to initialize a counter. If the person does exist, then increment by 1.
    for candidate in votes_list:
        if candidate not in votes_dict:
            votes_dict[candidate] = 0
            votes_dict[candidate] = votes_dict[candidate] + 1
        else:
            votes_dict[candidate] = votes_dict[candidate] + 1
    #print(votes_dict)
    
    # Loop 3: Find the winner by looping thru the dictionary for the highest value
    
    winner = ["", 0]
    for k,v in votes_dict.items():
        #print(k , v)
        if v > winner[1]:
            winner[1] = v
            winner[0] = k
            
    print(winner)
    
    # Calculations of Candidate Percentages
    khan = votes_dict["Khan"] / total_votes
    Correy = votes_dict["Correy"] / total_votes
    Li = votes_dict["Li"] / total_votes
    OTooley = votes_dict["O'Tooley"] / total_votes
    
    

output = (
    f"Election Results:\n"
    f"--------------------------------------------\n"
    f"Total Votes From Elections: {total_votes}\n"
    f"--------------------------------------------\n"
    f"Khan: {khan}\n"
    f"Correy: {Correy}\n"
    f"Li: {Li}\n"
    f"O'Tooley: {OTooley}\n"
    f"--------------------------------------------\n"
    f"Winner: {winner}\n"
    f"--------------------------------------------\n"
    )

with open ("election_results.txt", 'w') as txt_file:
    txt_file.write(output)

