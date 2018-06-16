# This profram allows the user to choose various
# geometry calculations form a menu. This program
# imports the circle and recangle modules.

import circle
import rectangle

# Constants for the menu choices
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

# The main function.
def main():
    # the choice variable controls the loop
    # and holds the user's menu choice
    choice = 0
    
    while choice != QUIT_CHOICE:
        # Display the menu.
        display_menu()
        
        # Get the user's choice.
        choice = int(input('Enter your choice: '))
        # Preform the selected action.
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input('Enter the circle\'s radius: '))
            print('The area is', circle.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input('Enter the circle\'s radius: '))
            print('The circumfrenece is', \
            circle.circumference(radius))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input('Enter the recangle\'s width: '))
            length = float(input('Enter the recangle\'s length: '))
            print('The perimeter is', \
            rectangle.perimeter(width, length))
        elif choice == QUIT_CHOICE:
            print('Exiting the program...')
        else:
            print('Error: invalid selection.')
# The display_menu function displays a menu.
def display_menu():
    print(' \t\tMENU')
    print('1) Area of a circle')
    print('2) circumference of a circle')
    print('3) Are of a recangle')
    print('4) Perimeter of a recangle')
    print('5) Quit')

# Call the main function
main() # end of program