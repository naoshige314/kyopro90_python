import math
a,b=map(int,input().split())

#a,bの最小公倍数は、a,bの最大公約数gcdを求めて、a*b/gcd(a,b)

g=math.gcd(a,b)

ans=a*b//g

if ans > 10**18:
    print('Large')
else:
    print(ans)