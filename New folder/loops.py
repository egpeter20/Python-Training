# The while Loop: A Condition-Controlled Loop 

# This program calculates sales commissions.
# Creat a variable to control the loop.
keep_going = 'y'

# Calculate a series of commissions

while keep_going == 'y':
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))
    
    # Calculate the commission
    commission = sales * comm_rate
    
    # Display the commission.
    print('The commisssion is $', \
    format(commission, ',.2f'), sep='')
    
    # See if the user wants to do another one.
    keep_going = input('Do you want to calculate another' + \
                'commission (Enter y for yes): ')
    if keep_going != 'y':
    
    
# End of program


print ('\n')


# The for Loop: A Count-Controlled Loop

for num in[0, 1, 2, 3, 4, 5]:
    print(num)
    
print ('\n')

for name in ['Peter', 'Initial', 'Botros']:
    print(name)

print ('\n')

for numbers in range(5): # range is a kay word
    print(numbers)
    
print ('\n')

for x in range(5):
    print('Welcome all')
    
print ('\n')

for num in range(1, 10, 2):
    print(num)

print ('\n')

# This program uses a loop to display a table showing
# the numbers 1 through 10 and their squares.

print('This program displays a list of numbers')
print('(starting at 1) and their squares.')
end = int(input('How high should I go? '))

# Print the table headings
print('Number\tSquare')
print('--------------')

# Print the numbers 1 through 10, and their squares
for number in range(1, end+1):
    square = number**2
    print(number, '\t', square)

# End of program