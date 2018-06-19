# This program gets employee data from the user and 
# save it as records in the employee.txt file.

def main():
    # Get the number of employee records to create.
    num_emps = int(input('How many employee records '+ \
    'do you want to creat? '))
    
    # Open a file for writing.
    emp_file = open('employees.txt', 'w')
    
    # Get each employee's data and write it to the file
    for count in range(1, num_emps + 1):
        # Get the data for an employee.
        print('Enter data for employee #', count, sep='')
        name = input('Name: ')
        id_num = input('ID number: ')
        dept = input('Department: ')
        
        # Write the data for an employee.
        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')
        
        # Display a blank line.
        print()
        
    # Close the file.
    emp_file.close()
    print('Employee records written to employees.txt.')
    print()
    print('Reading From Employee records employees.txt.')
    
    # Reading the data from the file!
    emp_file = open('employees.txt', 'r')
    
    name = emp_file.readline()
    
    while name != '':
        
        # read the id
        id_num = emp_file.readline()
        
        # read the dept
        dept = emp_file.readline()
        
        # Strip the newlines from the fields.
        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')
        
        
        # Display the record.
        print('Name:', name)
        print('ID:', id_num)
        print('Dept:', dept)
        print()
        
        name = emp_file.readline()
        
    # Close the file!
    emp_file.close()
        
        
# Call the main function
main()