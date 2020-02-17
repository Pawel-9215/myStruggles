# serching for prime
#testing 123 456a ee
#inp1 = "3 4000"
import math
import random
from random import randint


known_primes = []


s = """
"""

def is_prime_hard(num):
  
   # Corner cases 
    if (num <= 1) : 
        return False
    if (num <= 3) : 
        return True
   
      # This is checked so that we can skip  
      # middle five numbers in below loop 
    if (num % 2 == 0 or num % 3 == 0) : 
        return False
   
    i = 5
    while(i * i <= num) : 
        if (num % i == 0 or num % (i + 2) == 0) : 
            return False
        i = i + 6
   
    return True



for i in range(0, 20):
   if is_prime_hard(i) == True:
      known_primes.append(i)



def main(inp1):
    borders = []
    inp_list = []

    table_of_primes = []

    for num in inp1.split():
        borders.append(int(num))

    for i in range(borders[1]+1):
        table_of_primes.append(True)
    #print("table after spawning ", table_of_primes)

    prime_suspect = 2

    while(prime_suspect**2 <= borders[1]):
        if (table_of_primes[prime_suspect]==True):
            for i in range(prime_suspect**2, borders[1]+1, prime_suspect):
                table_of_primes[i] = False
        prime_suspect += 1

    for p in range(borders[0], borders[1]):
        if table_of_primes[p]:
            inp_list.append(str(p))

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

            