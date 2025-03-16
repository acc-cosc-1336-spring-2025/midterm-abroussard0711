#add import

import question_d

def main ():
    
    quit_program = False       # flag to control the while loop

    while not quit_program:
        get_day = input ('Enter a number 1 through 7, or type "quit" to exit: ')     # to prompt user input

        if get_day.lower() == 'quit':           # exit option
            print ("Exiting program...")
            quit_program = True                 # update flag to exit the while loop

        elif get_day.isdigit():                 # to validate numerical input
            user_number = int (get_day)         # assign the input as an integer
            result = question_d.get_day_of_week (user_number)   # to call the get_day_of_week decision function
            print (result)

main ()