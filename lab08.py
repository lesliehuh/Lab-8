#Leslie Huh
#Lab 08
prime_list=[]
d=2
number = 0
def is_prime(n):
    """ is_prime is a function that determines whether or not a number is prime 
    It works by determining if the number is divisible by anything other than 1 or itself. 
    It does this by making sure everything has a remainder of more than 0 and makes sure that
    once the divisor is equal to the number being divided, it ends the function and returns True"""
    global d
    if n%d == 0:
        return False
    elif n == d:
        return True
    else:
        d+=1
        is_prime(n)
    
def find_prime():
    """ findprime is a function dedicated to finding the 10001st prime number
    It does this by determining whether all number leading up to the 10001st prime number
    are prime or not, putting it into a list to be able to determine when to return 
    the number instead of continuing. """
    global number
    if len(prime_list)==10001:
        return prime_list[10000]
    else:
        if is_prime(number) == True:
            prime_list.append(number)
            number += 1
            prime_list()
        else:
            number +=1
            find_prime() 

print(find_prime())