L,R=map(int,input().split())
MOD=10**9+7

#桁数を求める
def dig(n):
    for i in range(1,20):
        if 10**(i-1) <= n and n <= 10**i-1:
            break
    
    return i

#等差数列の和(初項、末項、項数)
def s_diff(a,l,n):
    return (n*(a+l)//2)%MOD



dL=dig(L)
dR=dig(R)
ans=0
#print(L,R,dL,dR)
#解の足し合わせ

for k in range(dL,dR+1):
    #初項と末項と項数の計算
    a=10**(k-1)
    l=10**k-1
    if k == dL:
        a=L
    if k == dR:
        l=R
    n=l-a+1
    #桁数k × その桁で書かれている文字数の和
    ans += k*s_diff(a,l,n)
    ans %= MOD

print(ans)