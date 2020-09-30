import os
import csv

analysis_csv = os.path.join("Resources", "budget_data.csv")

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

print (total)
print (netchange)
print (average_change)
print (greatest_increase)
print ("is the greatest increase and is on")
print (date_increase)
print (greatest_decrease) 
print ("is the greatest decrease and is on")
print (date_decrease)