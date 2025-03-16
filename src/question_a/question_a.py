#write functions here, don't add input('') statements here!
def test_config():
    return True

# to create a void function that assigns a number to its local variable 'num' but doesn't return a value
def use_local_variable (num):
    num = 10

# to create a test function that assigns a number to its local variable, calls the void function, and returns the value of its local variable
def test_case ():
    num = 100
    use_local_variable(num)
    return num
    