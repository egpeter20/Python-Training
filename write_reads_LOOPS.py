# This program promprs the user for sales amounts
# and writes those amounts to the sales.txt file

def main():
    
    # Get the number of days.
    num_days = int(input('For how many days do ' + \
    'you have sales? '))
    
    # Opne a new file names sales.txt
    sales_file = open('sales.txt', 'w')
    
    # Get the amount of sales for each day and write
    # it to the file.
    for count in range(1, num_days + 1):
        # Get the sales for a day.
        sales = float(input('Enter the sales for day #' + \
                str(count) + ': '))
                
        # Write the sales amount to the file.
        sales_file.write(str(sales) + '\n')
        
    # Close the file.
    sales_file.close()
    print('Data written to slaes.txt.')
    
    # Reading from file using While loop
    print ('\n\tRead all of the values in the sales file using While loop.')
    
    # Open the file
    sales_file = open('sales.txt', 'r')
    
    # Reading the first line
    line = sales_file.readline()
    
    while line != '':
        amount = float(line)
        
        print(format(amount, ',.2f'))
        
        line = sales_file.readline()
        
    sales_file.close()
        
    # Reading from file using For loop
    print ('\n\tRead all of the values in the sales file using For loop.')

    # Open the file
    sales_file = open('sales.txt', 'r')
    
    # Reading using the For loop
    for line in sales_file:
        
        amount = float(line)
        
        print(format(amount, '.2f'))
        
    # Close the file.
    sales_file.close()
        
# Call the main function.
main()