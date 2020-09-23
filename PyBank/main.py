import csv
import os

#set path to the budget_data.csv which is in the resources folder
budget_data_path = os.path.join("Resources","budget_data.csv")

#create lists for the change in profit/loss and for date
change_profitloss = []
date_profitloss = []

#in the csv file
with open(budget_data_path) as budgetfile:   

    budgetcsvreader = csv.reader(budgetfile, delimiter = ",")

    #get the header row
    budgetcsv_header = next(budgetcsvreader)

    #get the first row after header row so as to initialize values
    row = next(budgetcsvreader)
    
    #initialize total_months to 1 for first row
    total_months = 1

    #initialize net_total variable to first row's profit/loss
    net_total = int(row[1])

    #initialize previous_row_profitloss to first row's profit/loss
    previous_row_profitloss = int(row[1])

    #for each row
    for row in budgetcsvreader:
        
        #calculate the total number of rows
        total_months = total_months + 1

        #get the current row's profit/loss value as integer
        current_row_profitloss = int(row[1])

        #find net total
        net_total = net_total + current_row_profitloss

        #find the difference between current row's profit/loss and previous row's profit/loss and add to list
        change_profitloss.append(current_row_profitloss - previous_row_profitloss)

        #add the current row's year to list
        date_profitloss.append(row[0])
        
        #set previous_row_profitloss to cureent row's profit/loss
        previous_row_profitloss = current_row_profitloss

    #find greatest increase in profits
    great_profit = max(change_profitloss)
    
    #find the year with greatest increase in profits
    great_profit_year = date_profitloss[change_profitloss.index(great_profit)]
    
    #find greatest decrease in losses
    great_loss = min(change_profitloss)  
    
    #find the year with greatest decrease in losses
    great_loss_year= date_profitloss[change_profitloss.index(great_loss)]
    
    #find the average change in profit/loss
    average_change = round(sum(change_profitloss)/(len(change_profitloss)),2)

    #create a list to print the financial analysis
    line = ["Financial Analysis"]
    line.append("----------------------------")
    line.append("Total Months: " + str(total_months))
    line.append("Total: " + str(net_total))
    line.append("Average  Change: " + str(average_change))
    line.append("Greatest Increase in Profits: "+ str(great_profit_year) + " $" + str(great_profit))
    line.append("Greatest Decrease in Profits: " + str(great_loss_year) + " $" + str(great_loss))

    #print analysis to terminal
    print("\n".join(line))

    #export the analysis to a text file
    output_path = os.path.join("Analysis","Finanlcial_Analysis.txt")

    with open(output_path,"w") as analysisfile:

        #write the financial analysis to the file
        analysisfile.writelines("\n".join(line))
        
