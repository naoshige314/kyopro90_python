import math

k=int(input())

#素因数分解 O(sqrt(N))
def prime_factorization(a):
    sqa=math.ceil(math.sqrt(a))
    c=a
    ret=[]
    for i in range(2,sqa+1):
        while c % i == 0:
            ret.append(i)
            c = c // i
    
    if c != 1:
        ret.append(c)
    
    return ret

pri=prime_factorization(k)

#print(pri)
