import itertools
n,p,q=map(int,input().split())

a=list(map(int,input().split()))

for i in range(n):
    a[i]%=p

ans=0
for ite in itertools.combinations(a,5):
    #計算途中で2^63-1を超えると時間かかる
    #tmp=(ite[0]*ite[1]*ite[2]*ite[3]*ite[4])%p だとTLE
    tmp=ite[0]*ite[1]%p*ite[2]%p*ite[3]%p*ite[4]%p
    if tmp == q:
        ans += 1

print(ans)