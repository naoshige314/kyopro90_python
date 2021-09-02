import math
K=int(input())
#約数列挙

def divisor(n):
    sqn=math.floor(math.sqrt(n))
    ret=[]
    for i in range(1,sqn+1):
        if n % i:
            continue
        ret.append(i)
        if i != n // i:
            ret.append(n // i)
        
    ret.sort()
    return ret



divs=divisor(K)

#print(divs)
#a,bの全探索
ans=0
l=len(divs)
for i in range(l):
    for j in range(i,l):
        a=divs[i]
        b=divs[j]
        if a > b:
            continue
        if K % (a * b):
            continue
        c = K // (a*b)
        if b > c:
            continue
        ans += 1

print(ans)