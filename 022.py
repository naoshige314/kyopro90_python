import math
a,b,c=map(int,input().split())

ab=math.gcd(a,b)
gcd3=math.gcd(ab,c)

ans=a//gcd3 + b//gcd3 + c//gcd3 - 3
print(ans)