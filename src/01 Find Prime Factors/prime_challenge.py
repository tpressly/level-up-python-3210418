from math import sqrt as sqrt

# challenge return all prime factors (including duplicates) as a list
# a*b*c*d*e = number
def get_prime_factors(bigNum):
    if not isinstance(bigNum, int): return "Error"
    if bigNum < 2: return "Error"
    myList = list()
    sqrtNum = int(sqrt(bigNum))+1
    keepLooping = True
    while keepLooping:
        factor = get_factor(bigNum, sqrtNum)
        if factor is not None:
            myList.append(factor)
            bigNum = int (bigNum / factor)
            if sqrtNum > 3: 
                keepLooping = True
            else:
                keepLooping = False
        else:
            keepLooping = False

    if bigNum > 1: myList.append(int(bigNum))
    return myList

def get_factor(Num, sqrtNum):
    factor = None
    #print(Num, sqrtNum)
    for i in range(2, sqrtNum, 1):
        #print(i)
        if ((int(Num) % i ) == 0) : 
            factor = i
            break
        else:
            continue
    return factor
    

print(get_prime_factors(630))
