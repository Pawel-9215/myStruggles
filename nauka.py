# serching for prime
#testing 123 456a ee
#inp1 = "3 4000"
import math



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
    global known_primes
    new_known_primes = []
    
    for num in inp1.split():
        borders.append(int(num))

    #print(borders)
    #print(type(borders))
    prime_suspect = borders[0]
    known_primes_included = False


    while prime_suspect < known_primes[0]:
        if is_prime_hard(prime_suspect) == True:
            inp_list.append(str(prime_suspect))
            new_known_primes.append(prime_suspect)
        if prime_suspect < borders[1]:
            prime_suspect += 1
        else:
            known_primes = known_primes+new_known_primes
            return inp_list

    if borders[0] >= known_primes[0] >= borders[1] or borders[0] <= known_primes[-1] <= borders[1]:
        known_primes_included = True
    else:
        known_primes_included = False
    
    if known_primes_included == True:
        iteration = 0
        while known_primes[iteration] < borders[0]:
            iteration += 1

        while known_primes[iteration] < borders[1]:
            inp_list.append(str(known_primes[iteration]))
            if iteration < len(known_primes)-1:
                iteration += 1
                prime_suspect = known_primes[iteration]
            else:
                #inp_list.append(str(known_primes[-1]))
                prime_suspect = known_primes[-1] + 1
                break

    while prime_suspect <= borders[1]:
        if is_prime_hard(prime_suspect) == True:
            inp_list.append(str(prime_suspect))
            new_known_primes.append(prime_suspect)
        if prime_suspect < borders[1]:
            prime_suspect += 1
        else:
            known_primes = known_primes+new_known_primes
            return inp_list

    known_primes = known_primes+new_known_primes
    return inp_list


    


    #print(s.join(inp_list))
    #print("")

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
    known_primes.sort()
    print(s.join(main(ranges)))
    print("")

            