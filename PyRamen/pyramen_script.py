import csv #import csv library so we can parse the CSV file


####
#GLOBAL VARIABLES
####
menu = [] #define empty list to store values from the CSV file
sales = [] #define empty list to store values from the CSV file
report = {} #define empty dictionary to store the aggregated per-product results


####
#IMPORT DATA
####
with open('menu_data.csv', newline='') as menu_data: #open the menu_data.csv with the variable menu_data
    menu_reader = csv.reader(menu_data) #use the `reader` function from the `csv` library to begin reading the data
    header = next(menu_reader) #use the `next` function to skip the header
    for row in menu_reader:
        menu.append(row) #add each row of the data to the menu list

with open('sales_data.csv', newline='') as sales_data: #open the sales_data.csv with the variable sales_data
    sales_reader = csv.reader(sales_data) #use the `reader` function from the `csv` library to begin reading the data
    header = next(sales_reader) #use the `next` function to skip the header
    for row in sales_reader:
        sales.append(row) #add each row of the data to the sales list


####
#FUNCTIONS
####
#create a nested loop by looping through every record in `menu`
def sales_analysis():
    for row in sales:
        quantity = int(row[3])
        sales_item = row[4]

        if sales_item not in report:
            report[sales_item] = {'01-count':0, '02-revenue':0, '03-cogs':0, '04-profit':0}

        #create a nested loop by looping through every record in `menu`
        for row in menu:
            item = row[0]
            price = float(row[3])
            cost = int(row[4])

            if sales_item == item:
                quantity = quantity
                price = price
                cost = cost
                report[sales_item]["01-count"] += quantity
                report[sales_item]["02-revenue"] += price * quantity
                report[sales_item]["03-cogs"] += cost * quantity
                report[sales_item]["04-profit"] += (price-cost) * quantity


###
#PRINT RESULTS TO TERMINAL
###
def print_results():
    sales_analysis()
    print(report)


###
#WRITE RESULTS TO CSV FILE
###
#create a funtion to write the results to a text file
def write_results():
    with open('PyRamen_Results_Script.txt', 'w') as file: #open a file in write mode and write the desired output
        file.write(str(report))


#create a function to run the script
def run_pyramen_script():
    print_results() #call function to print results to terminal
    write_results() #call function to write results to text file

run_pyramen_script() #call function to run script