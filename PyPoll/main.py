#this brings in some libraries to use
import csv
import os

#this tells the computer where to look, going back up one folder and then into resources and budget_data.csv
csvpath = os.path.join("Resources", "election_data.csv")

#this opens the declared value as a csvfile
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    
    #this moves past the first row/headers
    csv_header = next(csvreader)

    #this creats a dictionary list
    candidate_dictionary = {}
    #this starts the first row number as 0
    row_number = 0

    #this implies that this loop will repeat for the number of rows in csvreader
    for row in csvreader:
        #this states that for every loop, row_number will increase by one, making it progress by one each time
        row_number +=1
        #this states that if the value that is in row[2] is in the dictionary, and one vote to that candidate
        if row[2] in candidate_dictionary:
            candidate_dictionary[row[2]] += 1
        #this states that if the value in row[2] is not in the dictionary, it's a new candidate and add 1 vote
        else:
            candidate_dictionary[row[2]] = 1

    print(candidate_dictionary)

    #this states that wherever the loop ended, that row_number value now equals the Total_Votes
    Total_Votes = row_number

    #this formats the results
    print("Election Results")

    #this prints a visual line break
    print("-------------------------")
    
    #this prints the Total_Votes value, preceded by "Total Votes"
    print(f"Total Votes: {Total_Votes}")

    #this prints a visual line break
    print("-------------------------")


    #this loops through the number of values in candidate_dictionary
    for candidate_stats in candidate_dictionary:

        #this prints each value in the candidat_dictionary and adjusts to the format of the desired output
        print (f"{candidate_stats}: {round((candidate_dictionary[candidate_stats]/Total_Votes*100),2)}00% ({int(candidate_dictionary[candidate_stats])})")

    #this prints a visual line break
    print("-------------------------")

    #this pulls the max value from the candidate_dictionary and stores it as winner
    winner = max(candidate_dictionary, key = candidate_dictionary.get)  

    #this prints the variable winner
    print(f"Winner: {winner}")

