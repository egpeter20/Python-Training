# This program demonstrates how numbers
# must be converted to strings before they
# are written to a text file.

def main():
    # Open a file for writing.
    outFile = open('numbers.txt', 'w')
    
    # Get three numbers to the file.
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    num3 = int(input('Enter another number: '))
    
    # Write the numbers to the file.
    outFile.write(str(num1) + '\n')
    outFile.write(str(num2) + '\n')
    outFile.write(str(num3) + '\n')

    
    # Close the file.
    outFile.close()
    
    print('Data written to numbers.txt')

    # Open the file and sum its numbers
    inFile = open('numbers.txt', 'r')
    
    num1 = int(inFile.readline())
    num2 = int(inFile.readline())
    num3 = int(inFile.readline())
    
    total = num1 + num2 + num3
    
    print('The sum is ', total)
    
    
main()