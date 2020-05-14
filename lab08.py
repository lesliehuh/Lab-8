#Leslie Huh
#Lab 08
""" This for loop finds the 10001st prime number.

    The for loop determines if a number is a prime numebr or not by brute forcing
    division. If the number is a prime number, the count increases. If the count is
    10001, then it is the 10001st prime number. It then prints the number """


count = 3
x = 4
while count <= 10001:
    for i in range (2, x+1):
        if x%i==0 and x != i:
            x += 1
            break
        elif x==i:
            count += 1
            x += 1

print (x-1)

