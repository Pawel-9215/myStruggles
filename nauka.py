# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

A = [1, 3, 6, 6, 4, 1, 2, 1, 1, 1, 4, 4, 4, 4, 4, 4, 5, -3, 7, 8, 8]

def solution(A):
    
    positives = [item for item in A if item > 0]
    search = 1
    counter = 0
    s = True

    if len(positives) == 0:
        return 1
    
    positives.sort()
    maxlen = len(positives)-1

    while s == True:
 
        if positives[counter] == search:
            counter = check_next(positives, counter, search, maxlen)
            search += 1
            if counter > maxlen:
                return search
        else:
            return search

            
    
def check_next(positives, counter, search, maxlen):

    if counter > maxlen:
        return counter
    else:
        while positives[counter] == search:
            counter += 1
            if counter > maxlen:
                return counter

        return counter

print("solution:")
print(solution(A))
