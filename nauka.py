# serching for prime
#testing 123 456a ee
#inp1 = "3 4000"
import math
from math import floor, sqrt
import random
from random import randint


known_primes = []


s = """
"""



def main(inp1):
    borders = []
    inp_list = []
    global known_primes 
    table_of_primes = []

    for num in inp1.split():
        borders.append(int(num))

    for i in range(borders[1]+1):
        table_of_primes.append(True)
    limit = floor(sqrt(borders[1])) + 1

    
    
    prime_suspect = 2

    while(prime_suspect**2 <= limit):
        if (table_of_primes[prime_suspect]==True):
            for i in range(prime_suspect**2, limit+1, prime_suspect):
                table_of_primes[i] = False
        prime_suspect += 1

    for p in range(borders[0], limit):
        if table_of_primes[p]:
            inp_list.append(str(p))
            known_primes.append(p)
    print(known_primes)

    #print("table after loop ", table_of_primes)
    return inp_list

list_inp1 = []
how_many = int(input("How many ranges will you give me?: "))
#print(type(how_many))
for i in range(1, how_many+1):
    list_inp1.append(input("enter range: "))
for ranges in list_inp1:
    known_primes.sort()
    print(s.join(main(ranges)))
    print("")

            