#PyBank_Code

import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#join csv
csv_path = os.path.join ('Resources', 'budget_data.csv')

month = 0
total_profits = 0
Total_change = 0
Monthly_change = 0
max_change = -9999 #arbitrarily small number
min_change = 9999 #arbitrarily large number
min_month = 0
max_month = 0


#open, then read the csvfile
with open(csv_path) as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=',')
    next(csv_reader)
    

    #run the loop for the rows in CSV_reader
    for row in csv_reader:

        #Add previous month + 1 to get total # of months
        month = month + 1
        #Find total profits by adding up the p/l column (2nd column, but python 
        # starts with 0, so [1] represents the second column in the series)
        total_profits = int(row[1]) + total_profits
        Current_row = int(row[1])

        #Month>1 b/c January did not have a month before it, so it should
        #start when the counter is greater than 1
        if month >1:
            #to find the avg change, we need a monthly change variable
            Monthly_change = (Current_row - Previous_row)
            #then all of the monthly changes in a total change variable
            Total_change = Total_change + (Monthly_change)
        Previous_row = Current_row

            #for loop that finds the highest/lowest monthly change to find
            #greatest increase and decrease in profits            
        if Monthly_change > max_change:
            max_change = Monthly_change
            max_month = row[0] 
                
        if Monthly_change < min_change:
            min_change = Monthly_change
            min_month = row[0] 

print("PyBank Financial Analysis")
print("-------------------------------")
print(f"Total Months : {month}")
print(f"Total Profits : ${total_profits}")
print(f"Average Change : ${Total_change/85:.2f}")
print(f"Greatest Increase in Profits : {max_month} (${max_change})")
print(f"Greatest Decrease in Profits : {min_month} (${min_change})")


output = os.path.join("Analysis_PyBank", "Results_file.txt")
with open(output,'w') as text:
    text.write("PyBank Financial Analysis\n")
    text.write("-------------------------------\n")
    text.write(f"Total Months : {month}\n"
    f"Total Profits : ${total_profits}\n"
    f"Average Change : ${Total_change/85:.2f}\n"
    f"Greatest Increase in Profits : {max_month} (${max_change})\n"
    f"Greatest Decrease in Profits : {min_month} (${min_change})"
    )