#Leslie Huh
#Lab 08
prime_list=[]
d=2
number = 0
def is_prime(n):
    global d
    print(d)
    if n%d == 0:
        return False
    elif n == d:
        return True
    else:
        d+=1
        is_prime(n)
    
def find_prime():
    global number
    print(number)
    if len(prime_list)==10001:
        return prime_list[10000]
    else:
        if is_prime(number) == True:
            prime_list.append(number)
        else:
            number +=1
            find_prime() 

print(find_prime())