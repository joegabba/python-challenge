#Get dependencies
import os
import csv 

#Set file Path

data_csv = os.path.join("..", "python-challenge", "recources", "budget_data.csv")

#List to store Data
profit = []
monthly_changes = []
date = []

#Creating variables 
 
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

#Opening the csv file from the path for reading

#With open (budget_data.csv) as csvfile:
with open(data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the headers
    cvs_header = next(csvreader)

    #For loop to append List and calculate the variables
    for row in csvreader:
        count = count + 1
        date.append(row[0])
        profit.append(int(row[1]) -1)
        total_profit += int(row[1])

        final_profit = int(row[1])

        monthly_change_profits = final_profit - initial_profit
        monthly_changes.append(monthly_change_profits)
        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit

        average_change_profits = (total_change_profits/count)

        #Find greatest increase and Decrease
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)
        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

    
    print("========---Financial Analysis of ByPank===================----")
    print("               Total Months: " + str(count))
    print("               Total Profits: " + "$" + str(total_profit))

    print("               Average Change: " + "$" + str(int(average_change_profits)))
    
    print("               Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("               Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    
       
      

with open('Data.txt', 'w') as text:
    text.write("The Financial Data Analysis Of ByPank\n""\n")
    
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
   






        