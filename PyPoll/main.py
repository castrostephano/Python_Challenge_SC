#PyPoll_Code

import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#join csv
csv_path = os.path.join ('Resources', 'election_data.csv')

vote = 0
Khan_count = 0 
Correy_count = 0
Li_count = 0
OTooley_count = 0
Khan_per = 0 
Correy_per = 0
Li_per = 0
OTooley_per = 0
winner_vote = -9999 #arbitrarily small number
winner = 0


#open, then read the csvfile
with open(csv_path) as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=',')
    next(csv_reader)
    

    #run the loop for the rows in CSV_reader
    for row in csv_reader:

        #Add previous vote + 1 to get total # of votes
        vote = vote + 1
        Current_row = (row[2])

        if Current_row == "Khan":
            Khan_count = (Khan_count + 1)
            Khan_per = (Khan_count/vote*100) 

        if Current_row == "Correy":
            Correy_count = (Correy_count + 1)
            Correy_per = (Correy_count/vote*100) 

        if Current_row == "O'Tooley":
            OTooley_count = (OTooley_count + 1) 
            OTooley_per = (OTooley_count/vote*100) 

        if Current_row == "Li":
            Li_count = (Li_count + 1)
            Li_per = (Li_count/vote*100) 

        if Khan_count > winner_vote:
           winner = "Khan"
        
        elif Correy_count > winner_vote:
            winner = "Correy"
        
        elif OTooley_count > winner_vote:
            winner = "OTooley"
        
        elif Li_count > winner_vote:
            winner = "Li"


print("PyPoll Election Results")
print("-------------------------------")
print(f"Total votes : {vote}")
print("-------------------------------")
print(f"Khan: {Khan_per:.3f}% ({Khan_count})")
print(f"Correy: {Correy_per:.3f}% ({Correy_count})")
print(f"Li: {Li_per:.3f}% ({Li_count})")
print(f"O'Tooley: {OTooley_per:.3f}% ({OTooley_count})")
print("-------------------------------")
print(f"Winner: {winner}")
print("-------------------------------")



output = os.path.join("Analysis_PyPoll", "Results_file.txt")
with open(output,'w') as text:
    text.write("PyPoll Election Results\n")
    text.write("-------------------------------\n")
    text.write(f"Total Votes : {vote}\n"
    f"Khan: {Khan_per:.3f}% ({Khan_count})\n"
    f"Correy: {Correy_per:.3f}% ({Correy_count})\n"
    f"Li: {Li_per:.3f}% ({Li_count})\n"
    f"O'Tooley: {OTooley_per:.3f}% ({OTooley_count})\n")
    
    text.write(f"Winner: {winner}\n")

    text.write("-------------------------------")
    