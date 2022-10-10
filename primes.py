"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    num = 2
    while len(list) < number_of_primes:
        prime = True
        for x in range(1,num//2 + 1):
            if num % x == 0:
                prime = False
        if prime:
            list.append(num)
        num += 1
    return list
