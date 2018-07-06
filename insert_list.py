# This program demonstrates the isnert method

def main():
    # creat a list with some names.
    names = ['Peter', 'Ha', 'Bo']
    
    # Display the list.
    print('The list before the insert: ')
    print(names)
    
    # Insert a new name at the element 0
    names.insert(0, 'Remon')
    
    # Display the list again.
    print('The list after the insert: ')
    print(names)
    
# Call the main function
main()