# serching for prime
#testing 123 456a ee
#inp1 = "3 4000"
import math

known_primes = [2, 3, 5, 7, 11, 13]

def is_prime_easy(num):

    if num == 1:
        return False
    elif num % 2 == 0:
        return False
    elif num % 3 == 0:
        return False
    elif num % 5 == 0:
        return False
    else:
        return True

def is_prime_hard(num):

    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False

    return True






def main(inp1):
    borders = []
    inp_list = []
    global known_primes
    
    s = """
"""
    for num in inp1.split():
        borders.append(int(num))

    #print(borders)
    #print(type(borders))
    first_known_prime = 2
    last_known_prime = 3


    if borders[0] >= known_primes[0] and borders[0] <= known_primes[-1]:
        for prime in known_primes:
            if prime >= borders[0]:
                first_known_prime = known_primes.index(prime)
                break

        while known_primes[first_known_prime] <= borders[1] and first_known_prime <= (len(known_primes)-1):
            inp_list.append(known_primes[first_known_prime])
            first_known_prime += 1

    elif borders[1] >= known_primes[0] and borders[1] <= known_primes[-1]:
        for i in range(len(known_primes), 0, -1):
            if known_primes[i] >= borders[1]:
                last_known_prime = i
                break
        
        while known_primes[last_known_prime] >= borders[0] and last_known_prime >= 0:
            inp_list.append(known_primes[last_known_prime])
            first_known_prime -= 1
    


    print(s.join(inp_list))
    print("")

"""
    for i in range(borders[0], borders[1]+1):
        if i in known_primes:
            inp_list.append(str(i))
        elif is_prime_easy(i) == False:
            pass
        else:
            if is_prime_hard(i) == True:
                inp_list.append(str(i))
                known_primes.append(i)
"""                
    



list_inp1 = []
how_many = int(input("How many ranges will you give me?: "))
#print(type(how_many))
for i in range(1, how_many+1):
    list_inp1.append(input("enter range: "))
for ranges in list_inp1:
    main(ranges)

            