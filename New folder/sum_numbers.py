# This program calculates the sum of a series
# of numbers enterd by the user.

max = 5 # The maximum

# Initialize an accumulator variable.
total = 0.0

# Explain what we are doing.
print('This program calculates the sum of')
print(max, 'numbers your will enter. ')

# Get the numbers and accumulate them.
for counter in range(max):
    number = float(input('Enter a number: '))
    total += number
    
# Display the total of the numbers.
print('The total is ', total)
    
# End of program!