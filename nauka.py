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

    n = borders[1] - borders[0] + 1
    mark = [False]*(n+1)
    if ( borders[0] <= 1 ):
        borders[0] = 2;
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
    #print(mark)

    for i in range(len(known_primes)):
        loLim = floor(borders[0]/known_primes[i]*known_primes[i])
        if(loLim == known_primes[i]) :
            mark[loLim-borders[0]] = False
        if loLim < borders[0]:
            loLim += known_primes[i]
        if loLim == known_primes[i]:
            loLim += known_primes[i]

        for j in range(loLim, borders[1]+1, known_primes[i]):
            mark[j-borders[0]] = True
        
    for i in range(borders[0], borders[1]+1):
        if not mark[i-borders[0]]:
            known_primes.append(i)
            inp_list.append(str(i))

    #print("table after loop ", table_of_primes)



    print(known_primes)
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

            