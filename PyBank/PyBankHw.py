import os
import csv

# Path for file
csvpath = os.path.join('../Resources/budget_data.csv')

# Initial Variables

months = []
profit_loss = []


# Setting Fuction

def mean(numbers):
    return  float(sum(numbers)) / max(len(numbers),1)


# Open CSV File

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        
        # List for for each column
        months.append(row[0])
        profit_loss.append(int(row[1]))


    # Count for Months
    total_months = len(months)

    #total profit and loss

    total_profit_loss = sum(profit_loss)

    # Month to Month Change

    x = 1
    y = 0

    changes= []

    for month in range(total_months - 1):
        monthly_average = (profit_loss[x] - profit_loss[y])
        changes.append(int(monthly_average))
        x+=1
        y+=1
    
    avg_monthly_change = round(sum(changes)/(total_months -1), 2)


    # Max and Min

    min_change = min(changes)
    max_change = max(changes)

    change_max = changes.index(max_change)
    change_min = changes.index(min_change)

    min_month = months[change_min +1]
    max_month = months[change_max +1]
    
    # Output for Script
  
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(total_months))
    print("Total Profits: " + "$" + str(total_profit_loss))
    print("Average Change: " + "$" + str(int(avg_monthly_change)))
    print("Greatest Increase in Profits: " + str(max_month) + " ($" + str(int(max_change)) + ")")
    print("Greatest Decrease in Profits: " + str(min_month) + " ($" + str(int(min_change)) + ")")
    print("----------------------------------------------------------")
    
with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(total_months) + "\n")
    text.write("    Total Profits: " + "$" + (str(total_profit_loss)) +"\n")
    text.write("    Average Change: " + '$' + str(int(avg_monthly_change)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(max_month) + " ($" + str(int(max_change)) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(min_month) + " ($" + str(int(min_change)) + ")\n")
    text.write("----------------------------------------------------------\n")