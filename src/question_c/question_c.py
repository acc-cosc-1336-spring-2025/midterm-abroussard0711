#write functions here, don't add input('') statements here!

# to define the global variable
global_num = 80

# to define a function that calls the global variable, changes the value, and returns the new value
def use_global ():
    
    global global_num
    global_num = 25
    return global_num

# to define another function that calls the global variable, changes the value, and calls the first function to change it back
def change_global ():

    global global_num
    global_num = 100

    use_global ()

    return global_num

