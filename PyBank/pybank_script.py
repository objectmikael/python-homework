import csv #import csv library so we can parse the CSV file



####
#GLOBAL VARIABLES
####
dates = [] #define empty list to store Date values from the CSV file
profits_and_losses = [] #define empty list to store Profit/Losses values from the CSV file
change = [] #declare an empty list to hold the values of the Profit/Losses changes from month to month 



####
#IMPORT DATA
####
with open('budget_data.csv', newline='') as budget_data: #open the budget_data.csv with the variable budget_data
    budget_reader = csv.DictReader(budget_data) #convert the lines of the CSV file fo Python dictionaries
    for row in budget_reader:
        dates.append(row['Date']) #use the Date key to append values to the dates list 
        profits_and_losses.append(int(row['Profit/Losses'])) #use the Profit/Losses key to append values to the profits_and_losses list; converted values from strings to integers 



####
#FUNCTIONS
####
# define a function that calculates the number of entries in the data set and returns the value 
def total_months():
    return len(dates) #use the len method to count the number of elements in the dates list 

# define a function that calculates the net total amount of Profit/Losses in the data set and return the value
def net_total():
    sum_profits=sum(profits_and_losses) #use the sum method to calculate the sum total in the profits_and_losses list
    return sum_profits

# define a function that caluculates the average change in Profit/Losses in the data set and return the value, rounded to two decimal places
def avg_changes():
    for value in profits_and_losses:
        if value == profits_and_losses[0]: #if the value is equal to the the value in the index 0 of profits_and_losses, run the code block
            x1 = value #assign value to a variable x1
        elif value: #if a value exist, run the code block set it equal to value_x2
            x2 = value #assign value to a variable x2
            delta = x2 - x1 #calculate the difference of x2 and x1 and assign it to a variable delta
            change.append(delta) #add the value of delta to the change list
            x1 = x2 #reassign the x1 the value of x2
    return round((sum(change)/len(change)),2) #return the average, rounded to two decimal places

# define a function that identifies the index of the element with the highest delta in change list and returns both the Date and Total that corresponds 
def greatest_increase_in_profits():
    max_index = change.index(max(change)) #identify the index of the largest delta in the change list
    date = dates[max_index+1] #grab the corresponding date from the dates list
    amount = max(change) #grab the max value from the change list
    return [date, amount] #return both the date and amount variables in a list

# define a function that identifies the index of the element with the smallest delta in change list and returns both the Date and Total that corresponds 
def greatest_decrease_in_profits():
    min_index = change.index(min(change)) #identify the index of the smallest delta in the change list
    date = dates[min_index+1] #grab the corresponding date from the dates list
    amount = min(change) #grab the max value from the change list
    return [date, amount] #return both the date and amount variables in a list


###
#PRINT RESULTS TO TERMINAL
###

#create a function to print results 
def print_results():
    print('Financial Analysis')
    print('----------------------------')

    print(f'Total Months: {total_months()}')
    print(f'Total: ${net_total()}') 
    print(f'Average Change: ${avg_changes()}')
    print(f'Greatest Increase in Profits: {greatest_increase_in_profits()[0]} (${greatest_increase_in_profits()[1]})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_in_profits()[0]} (${greatest_decrease_in_profits()[1]})')

###
#WRITE RESULTS TO CSV FILE
###
#create a funtion to write the results to a text file
def write_results():
    with open('PyBank_Results_Script.txt', 'w') as file: #open a file in write mode and write the desired output
        file.write('Financial Analysis \n')
        file.write('---------------------------- \n')
        file.write(f'Total Months: {total_months()} \n')
        file.write(f'Total: ${net_total()} \n')
        file.write(f'Average Change: ${avg_changes()} \n')
        file.write(f'Greatest Increase in Profits: {greatest_increase_in_profits()[0]} (${greatest_increase_in_profits()[1]}) \n')
        file.write(f'Greatest Decrease in Profits: {greatest_decrease_in_profits()[0]} (${greatest_decrease_in_profits()[1]})')


#create a function to run the script
def run_pybank_script():
    print_results() #call function to print results to terminal
    write_results() #call function to write results to text file

run_pybank_script() #call function to run script