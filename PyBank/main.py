import os
import csv

analysis_csv = os.path.join("Resources", "budget_data.csv")
results_txt = os.path.join("Analysis", "results.txt")

# Lists to store data

net_change_list = []
profit_inc = []
loss_dec = []

total = 0
netchange = 0
greatest_increase=0
greatest_decrease=0
# with open as cvsfile:
with open(analysis_csv) as cvsfile:
    csvreader = csv.reader(cvsfile, delimiter=",")
    #skips the first row as it is the title
    header=next(csvreader)
    #stores jan data as it is in first row
    jan_data=next(csvreader)
    total = total + 1
    #assigns value to netchange variable
    netchange = netchange + int(jan_data[1])
    profit_inc = int(jan_data[1])
    date_decrease = str(jan_data[0])
    date_increase = str(jan_data[0])
    #assigns value to previous change as a initial data
    previous_change = int(jan_data[1])
    #for loop moves through all the rows in opened csv file
    Temp_read = int(jan_data[1])
    greatest_increase =0
    greatest_decrease =0
    for row in csvreader:
        #counter to calculate the total number of months
        total = total + 1
        #adds all the profit and loss numbers
        netchange = netchange + int(row[1])
        #creates a list of changes between the months
        change = int(row[1])-previous_change
        previous_change=int(row[1])
        net_change_list = net_change_list + [change]
        #reads the first line and sets variable
        if previous_change > Temp_read:
            greatest_increase = int(row[1])
            date_increase = str(row[0])
        
        if previous_change < Temp_read:
            greatest_decrease = int(row[1])
            date_decrease = str(row[0])

        Temp_read = previous_change


        
#sums all the changes and divides it by the total changes         
average_change = sum(net_change_list)/len(net_change_list)
with open(results_txt, "w") as textfile:
    total_result =  f"total is {total}\n"
    textfile.write(total_result)
    print (total_result)

    netchange_result =  f"netchange is {netchange}\n"
    textfile.write(netchange_result)
    print (netchange_result)

    average_change_result =  f"average change is {average_change}\n"
    textfile.write(average_change_result)
    print (average_change_result)

    greatest_increase_result =  f"greatest increase is {greatest_increase} on the date {date_increase}\n"
    textfile.write(greatest_increase_result)
    print (greatest_increase_result)

    greatest_decrease_result =  f"greatest decrease is {greatest_decrease} on the date {date_decrease}\n"
    textfile.write(greatest_decrease_result)
    print (greatest_decrease_result)
