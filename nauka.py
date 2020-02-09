# serching for prime

inp1 = "3 4000"

def is_prime_easy(num):

    if num == 1:
        return False
    if num == 3:
        return True
    elif num == 2 or num == 5:
        return Trues
    elif num % 2 == 0 or num % 2 == 0 or num % 5 == 0:
        return False
    elif num % 3 == 0:
        return False
    elif num % 5 == 0:
        return False
    else:
        return True

def is_prime_hard(num):

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


borders = []

def main(repeats, inp1)
    for num in inp1.split():
        borders.append(int(num))

    print(borders)
    print(type(borders))

    for i in range(borders[0], borders[1]+1):
        if is_prime_easy(i) == False:
            pass
        else:
            if is_prime_hard(i) == True:
                print(i)


