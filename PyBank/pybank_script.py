# import pandas and assign it to the variable pd
import pandas as pd 
# using pandas, import the .csv file containing the data and save it to a variable data
data = pd.read_csv('budget_data.csv') 

# define a function that calculates the number of entries in the data set and returns the value 
def total_months():
    return len(data)

# define a function that calculates the net total mount of Profit/Losses in the data set and return the value
def net_total():
    sum=data['Profit/Losses'].sum()
    return sum

# define a function that caluculates the average change in Profit/Losses in the data set and return the value, rounded to two decimal places
def avg_changes():
    change = data['Profit/Losses'].diff()
    avg_change = change.mean().round(2) 
    return avg_change

# define a function that creates a new column in the data set to store the change from one date to the next 
def add_change_column():
    data['Change']= data['Profit/Losses'].diff()

add_change_column()

# define a function that identifies the location of the entry with the highest value in the newly formed change column and returns both the date and amount in a list 
def greatest_increase():
    max_index = data['Change'].idxmax()
    date = data.loc[max_index, 'Date']
    amount = data.loc[max_index, 'Change']
    return [date, amount]

# define a function that identifies the location of the entry with the lowest value in the newly formed change column and returns both the date and amount in a list 
def greatest_decrease():
    min_index = data['Change'].idxmin()
    date = data.loc[min_index, 'Date']
    amount = data.loc[min_index, 'Change']
    return [date, amount]

print('Financial Analysis')
print('----------------------------')

print(f'Total Months: {total_months()}')
print(f'Total: ${net_total()}') 
print(f'Average Change: ${avg_changes()}')
print(f'Greatest Increase in Profits: {greatest_increase()[0]} (${greatest_increase()[1]})')
print(f'Greatest Decrease in Profits: {greatest_decrease()[0]} (${greatest_decrease()[1]})')

# creates a text file called PyBank_Results and writes the desired output to the file
with open('PyBank_Results_Script.txt', 'w') as file:
    file.write('Financial Analysis \n')
    file.write('---------------------------- \n')
    file.write(f'Total Months: {total_months()} \n')
    file.write(f'Total: ${net_total()} \n')
    file.write(f'Average Change: ${avg_changes()} \n')
    file.write(f'Greatest Increase in Profits: {greatest_increase()[0]} (${greatest_increase()[1]}) \n')
    file.write(f'Greatest Decrease in Profits: {greatest_decrease()[0]} (${greatest_decrease()[1]})')

# To run this script open a terminal, navigate to the PyBank directory and type: python pybank_script.py 
# The result will display in the terminal and create a text file called PyBank_Results_Script with the results