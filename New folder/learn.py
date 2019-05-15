# I'm new here
''''
-------- Chapter One and Two --------

room = 25

print ('I am staying at room ', room)

room = 50

print ('Now, i am stying at room', room)


# Working with inputing data from the user

first_name = input('First name: ')

last_name = input ('Last name: ')

print ('Hello', first_name, last_name)


pay_rate = float(input('What is your hourly pay rate? '))

name = str(input("what is your name: "))


# Get the user name, age and income
name = input("what's you name? ")
age = int(input("How old are you? "))
income = float(input ("What's your income? "))

# Display the user info
print('Here is the date you entered:')
print('Name:', name)
print('Age:', age)
print('Income', income)

# Assign a value to the salary variable
salary = 2500.5

# Assign a value to the bonus variabl
bouns = 1200.0

# Calculate the total pay by adding salary
pay = salary + bouns

# Display the pay
print('Your pay is ', pay)


-| +\ |- to write in the same line
print('Enter the amount ' +\ 
      'of sales for each '+\
      'day')
      
amount_due = 5000.0
monthly_payment = amount_due / 12
monthly_payment = 123456789.456

-| .2f |- for decimal point formating
print('The monthley payment is', \
      format(monthly_payment, '.2f'))
      
-| ,d |- Comma rules
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print('Your annual pay is $', \
       format(5000000, ',d'), \
       sep ='')
'''
