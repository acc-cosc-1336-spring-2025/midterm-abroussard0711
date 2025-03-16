#add import

import question_c

# define the main function to call the global value and display its value before and after being changed
def main ():

    print ('Value of the global variable before the use_global() function is called: ', question_c.global_num)

    question_c.use_global ()

    print ('Value of the global variable after the use_global() function is called: ', question_c.global_num)
    
main ()