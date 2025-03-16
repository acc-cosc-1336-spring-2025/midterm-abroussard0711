#add import

import question_b

# define and run the main program
def main ():
    
    quit_program = False       # flag to control the while loop

    while not quit_program:
        get_number = input ('Enter a number, or type "quit" to exit: ')     # to prompt user input

        if get_number.lower() == 'quit':        # exit option
            print ("Thanks for playing!")
            quit_program = True                 # update flag to exit the while loop

        elif get_number.isdigit():              # to validate numerical input
            user_number = int (get_number)

            if question_b.is_prime(user_number):    # to call the prime function
                print (user_number, "is a prime number! Hooray!")
            else:
                print (user_number, "is not a prime number.")
        
        else:                                   # to request a valid input
            print ("Invalid input. Please enter a valid number.")



main ()