
#this brings in some libraries to use
import os
import csv

#this tells the computer where to look, going back up one folder and then into resources and budget_data.csv
csvpath = os.path.join('Resources', 'budget_data.csv')

#this opens the declared value as a csvfile
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    
    #this moves past the first row/headers
    csv_header = next(csvreader)
    
    #declares both the months and the net to start at zero before the for loop
    months = []
    net = []
    dif = []

    #starts the for loop for each row in csvreader
    for row in csvreader:

        #this creates a list of months from the 0 column
        months.append(row[0])
        #this creates a list of monthly net from the 1 column
        net.append(int(row[1]))

    #this sums all of the values from the list of net
    total = sum(net)
    #this counts the number of months by using the len (length) function
    number_of_months = len(months)

    print(f"Finanacial Analysis")
    print(f"----------------------------")

    #prints a string and then the value for months    
    print (f"Total Months: {number_of_months}")

    #prints a string and then the net value
    print (f"Total: ${total}")

    #this skips to the first (0) row because you can't compare it to nothing. It continues throughout the duration of the length of the net list.
    for x in range(1, len(net)):
        #this creates a new list the compares each month to the next
        dif.append(net[x] - net[x-1])

    #this creates an average of the dif list, adding all and dividing by number of months. the -1 is because there is one more month than on the dif list.
    average_dif = sum(dif)/(number_of_months - 1)

    #this just defines truncate as the decimal value to a dollar/cents value, pulled from the internet
    def truncate(n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier

    #this tells me to use the aforementioned trancate function
    average_dif = truncate(average_dif, 2)

    # this prints the average_dif with a string that precedes it for explanation.
    print(f"Average Change: ${average_dif}")

    #this locates the maximum value in the dif list and declares it as "max"
    max = max(dif)
    #this prints the newly found "max," which is preceded by a string that explains the value.
    print(f"Greatest Increase in Profits: {months[dif.index(max)+1]} (${max})")

    #this locates the minimum value in the dif list and declares it as "min"
    min = min(dif)
    #this prints the newly found "min," which is preceded vy a string that explains the value.
    print(f"Greatest Decrease in Profits: {months[dif.index(min)+1]} (${min})")

#export as text

