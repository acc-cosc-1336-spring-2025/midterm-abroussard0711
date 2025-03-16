#write functions here, don't add input('') statements here!

# create a function to determine if a number is prime
def is_prime (num):
    
    if num < 2:  
        return False # numbers less than 2 are not prime
    
    for n in range (2, num): # loops from 2 to n-1, all numbers are divisible by itself
        if num % n == 0:
            return False    # found a divisor other than 1 and itself, not a prime number
    
    return True # no divisors found, the number is prime
    