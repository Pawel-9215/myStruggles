
import math

known_primes = []
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





print(known_primes)

