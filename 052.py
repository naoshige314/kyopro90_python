n=int(input())

MOD=10**9+7
ans=1

for i in range(n):
    a1,a2,a3,a4,a5,a6=map(int,input().split())
    tot=a1+a2+a3+a4+a5+a6
    ans *= tot
    ans %= MOD

print(ans)