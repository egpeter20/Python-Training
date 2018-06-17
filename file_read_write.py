# This program writes three lines of data
# to a file

def main():
# Writes three lines of data to a file

    # Open a file named philosophers.txt
    outFile = open('philosophers.txt', 'w')
    
    # Write the name of the three philosophers 
    # to the file
    outFile.write('Peter Botros\n')
    outFile.write('David Botros\n')
    outFile.write('Remon Botros\n')
    
    # Close the file
    outFile.close()
    
# Writes data form the user to a file
    
    # print('Enter the names of three friends.')
    # name1 = input('Friend #1: ')
    # name2 = input('Friend #2: ')
    # name3 = input('Friend #3: ')
    
    # # Write the names to the file.
    # myfile = open('friends.txt', 'w')
    
    # # Write the names to the file.
    # myfile.write(name1 + '\n')
    # myfile.write(name2 + '\n')
    # myfile.write(name3 + '\n')
    
    # # Close the file.
    # myfile.close()
    
    # print('\nThe names were written to friends.')
    
    # # Opening the file for reading purpose 
    # myfile = open('friends.txt', 'r')
    
    # # Object that reads the info form the file
    # file_contents = myfile.read()
    
    # # Printing the contents of the file
    # print(file_contents)
    
    # # Closing the file
    # myfile.close()
    
# Read data from a file
    # Open the file
    inFile = open('philosophers.txt', 'r')
    
    # Read the file's contents
    file_contents = inFile.read()
    
    # Print the data that was read into memory.
    print(file_contents)
    
    # Reading line by line form the object
    # line1 = inFile.readline()
    # line2 = inFile.readline()
    # line3 = inFile.readline()
    
    # Strip the \n from each string.
    # line1 = line1.rstrip('\n')
    # line2 = line2.rstrip('\n')
    # line3 = line3.rstrip('\n')
    
    # Close the file
    inFile.close()
    
    # print(line1)
    # print(line2)
    # print(line3)
    
# call main function
main() # end of main!