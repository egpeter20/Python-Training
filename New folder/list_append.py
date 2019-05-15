# This program demonstrates how the append
# method can be used to add items to a list.

def main():
    # first, cerat an empty list.
    name_list = []
    
    # Creat a vafriable to control the loop
    again = 'y'
    
    # Add some names to the list.
    while again == 'y':
        # Get the name from the user.
        name = input('Enter a name: ')
        
        # Append the name to the list.
        name_list.append(name)
        
        # Add another one?=
        print('Do you want to add anotehr name? ')
        again = input('y = yes, anything else = no: ')
        print()
        
    # Display the names that were entered.
    for name in name_list:
        print(name)
            
# Call the main function
main()
