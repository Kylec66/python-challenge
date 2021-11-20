import os
import csv

# Path for file
csvpath = os.path.join('../Resources/election_data.csv')

count = 0
candidates = []
unique_candidates = []
vote_count = []
vote_percentage = []

# Open CSV

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        # Total Vote Count
        count = count + 1

        # Candidate Lists
        candidates.append(row[2])

    for x in set (candidates):
        unique_candidates.append(x)

        # Votes per candidate
        y = candidates.count(x)
        vote_count.append(y)

        # Percent per candidate
        z = (y/count)*100
        vote_percentage.append(z)

    
    winner_count = max(vote_count)
    winner= unique_candidates[vote_count.index(winner_count)]

    print("-------------------------")
    print("Election Results")   
    print("-------------------------")
    print("Total Votes :" + str(count))    
    print("-------------------------")
    for i in range(len(unique_candidates)):
            print(unique_candidates[i] + ": " + str(vote_percentage[i]) +"% (" + str(vote_count[i])+ ")")
    print("-------------------------")
    print("The winner is: " + winner)
    print("-------------------------")


    with open('election_results.txt', 'w') as text:
        text.write("Election Results\n")
        text.write("---------------------------------------\n")
        text.write("Total Vote: " + str(count) + "\n")
        text.write("---------------------------------------\n")
        for i in range(len(set(unique_candidates))):
            text.write(unique_candidates[i] + ": " + str(vote_percentage[i]) +"% (" + str(vote_count[i]) + ")\n")
            text.write("---------------------------------------\n")
            text.write("The winner is: " + winner + "\n")
            text.write("---------------------------------------\n")