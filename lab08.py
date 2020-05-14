#Leslie Huh
#Lab 08
import sys
sys.setrecursionlimit(15000)
prime_list=[1]
d=1
number = 2
def is_prime(n):
    """ is_prime is a function that determines whether or not a number is prime 
    It works by determining if the number is divisible by anything other than 1 or itself. 
    It does this by making sure everything has a remainder of more than 0 and makes sure that
    once the divisor is equal to the number being divided, it ends the function and returns True"""
    global prime_list
    global d
    if len(prime_list) == 1:
        d=1
        return True
    elif len(prime_list)==d+1:
        d=1
        return True
    elif n%prime_list[d]==0:
        d=1       
        return False
    else:
        d+=1
        return is_prime(n)
    
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
            find_prime()
        else:
            number +=1
            find_prime() 
            

print (find_prime())
