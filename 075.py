#素因数分解する
import math
n=int(input())
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

primes=prime_factorization(n)
l=len(primes)
#print(l)
#print(primes)
ans=0
#while 2**ans <l:
#    ans += 1
for i in range(100):
    if 2**i >= l:
        ans=i
        break


print(ans)