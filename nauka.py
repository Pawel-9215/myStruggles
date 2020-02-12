# serching for prime
#testing 123 456
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
    

    for i in range(borders[0], borders[1]+1):
        if i in known_primes:
            inp_list.append(str(i))
        elif is_prime_easy(i) == False:
            pass
        else:
            if is_prime_hard(i) == True:
                inp_list.append(str(i))
                known_primes.append(i)
                
    print(s.join(inp_list))
    print("")



list_inp1 = []
how_many = int(input("How many ranges will you give me?: "))
#print(type(how_many))
for i in range(1, how_many+1):
    list_inp1.append(input("enter range: "))
for ranges in list_inp1:
    main(ranges)

            