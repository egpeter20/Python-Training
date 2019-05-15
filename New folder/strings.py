# main1() 8.1 Basic String Operations
# This program counts the number of times
# The letter T (uppercase or lowercase)
# appers in a string.

def main1():
    # Creat a varuable to use to hold the count.
    # The variable must start with 0.
    
    count = 0
    
    # Get a string from the user.
    my_string = input('Enter a sentence: ')
    
    # Count the Ts.
    for ch in my_string:
        if ch == 'T' or ch == 't':
            count+=1
            
    # Print the result.
    print('The letter T appears', count, 'times.')
    # End of main1()

# main2() 8.2 String Slicing
def main2():
    my_string = 'Roses are red'
    ch = my_string[6]
    print(ch)
    print() # Empty line
    print(my_string[0], my_string[6], my_string[10])
    print() # Empty line
    
    city = 'Boston'
    print(city[5]) # Testing if the index is out of range
    print() # Empty line
    
    index = 0
    while index < len(city):
     print(city[index])
     index += 1
     
    print() # Empty line
    
    message = 'Hello'+ ' ' + 'world'
    print(message)
    
    print() # Empty line

    # Using the slicing expressions
    # NOTE: String slices are also called substrings.
    full_name = 'Patty Lynn Smith'
    middle_name = full_name[6:10] # This is how to use the slices [6:10]
    print(middle_name)
    
    middle_name = full_name[:5]
    print(middle_name)
    
    print() # Empty line
    
    middle_name = full_name[11:]
    print(middle_name)
    
    print() # Empty line
    full_name = 'Patty Lynn Smith'
    my_string = full_name[:]
    print(my_string)
    print() # Empty line

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(letters[0:len(letters):2]) # len(letters) = 26
    # The third number inside the brackets is the step value. 
    # A step value of 2, as used in this
    # example, causes the slice to contain every second character
    # from the specified range in the string. 
    print() # Empty line

    full_name = 'Patty Lynn Smith'
    last_name = full_name[-5:]
    print(last_name)
    print() # Empty line
    # End of main2()

# main3 = 8.3 Testing, Searching, and Manipulating Strings
def main3():
    text = 'Four score and seven years ago'
    if 'seven' in text:
     print('The string "seven" was found.')
    else:
     print('The string "seven" was not found.')
     
    print() # Empty line
    
    names = 'Bill Joanne Susan Chris Juan Katie'
    if 'Pierre' not in names:
     print('Pierre was not found.')
    else:
     print('Pierre was found.')
     
    print() # Empty line
    
    country = 'Egypt'
    if 'Egypt' in country:
        print(country, 'is found')
    else:
        print(country, 'is not found')
    
    print() # Empty line
    
    currentYear = '2018ABC'
    if currentYear.isdigit():
        print(currentYear,'contain only numbers!')
    else:
        print(currentYear,'doesn\'t contain only numbers!')
        
    print() # Empty line

    string = 'Four score and seven years ago'
    position = string.find('seven')
    if position != -1:
     print('The word "seven" was found at index', position)
    else:
     print('The word "seven" was not found.')
    
    print() # Empty line
    
    print('Hello' * 5)
    
    # Create a string with multiple words.
    my_string = 'One two three four'
    
    # Split the string.
    word_list = my_string.split()
    
    # Print the list of words.
    print(word_list)
    
    print() # Empty line
    
    # Create a string with a date.
    date_string = '11/26/2014'
    
    # Split the date.
    date_list = date_string.split('/')
    
    # Display each piece of the date.
    print('Month:', date_list[0])
    print('Day:', date_list[1])
    print('Year:', date_list[2])
    
    # End of main3()


# Call main functions.
main1() # Calling main1
main2() # Calling main2
main3() # Calling main3