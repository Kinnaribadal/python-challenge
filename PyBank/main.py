import os
import csv

analysis_csv = os.path.join("Resources", "budget_data.csv")

# Lists to store data
Date = []
Profit_Loss = []
net_change_list = []
Profit_inc = []
Loss_dec = []

total = 0
netchange = 0
# with open as cvsfile:
with open(analysis_csv) as cvsfile:
    csvreader = csv.reader(cvsfile, delimiter=",")
    header=next(csvreader)
    jan_data=next(csvreader)
    total = total + 1
    netchange = netchange + int(jan_data[1])
    previous_change = int(jan_data[1])
    for row in csvreader:
        total = total + 1
        netchange = netchange + int(row[1])
        change = int(row[1])-previous_change
        previous_change=int(row[1])
        net_change_list = net_change_list + [change]
average_change = sum(net_change_list)/len(net_change_list)
print (total)
print (netchange)
print (average_change)