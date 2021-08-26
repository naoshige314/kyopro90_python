#WA
#組み合わせ計算(29)の前にMODを適用(18)してしまっているので

import sys
sys.setrecursionlimit(100000)
N,L=map(int,input().split())
MOD=10**9+7
#L段飛ばしを最高何回できるか
M=N//L

f=[0]*(N+1)
f[0]=1
f[1]=1

def fac(n):
    if f[n]:
        return f[n]
    f[n]=(n*fac(n-1))%MOD
    return f[n]



ans=1
for i in range(1,M+1):
    t=N-i*L#1段のぼる回数
    a=fac(t+i)
    b=fac(i)
    c=fac(t)
    tmp=(a//b)//c
    print(i,t,tmp)
    ans += tmp
    ans= ans%MOD

print(ans)
print(f)


