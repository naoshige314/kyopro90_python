n,k=map(int,input().split())
MOD=10**9+7
#ans=k*(k-1)*((k-2)**(n-2))%MOD
#これの計算時間を短縮する
#(n-2)を2の冪ごとに表し、k-2をその回数MODを入れつつかける


def calc_pow(a0,b):
    a=a0
    ret=1
    for i in range(61):
        if i:
            a=a*a
            a %= MOD
        if b&(1<<i):
            ret *= a
            ret %= MOD
    return ret

ans=0
if n==1:
    ans=k
elif n==2:
    ans=k*(k-1)
else:
    if k<3:
        ans=0
    else:
        ans=k%MOD*(k-1)%MOD*calc_pow(k-2,n-2)%MOD

print(ans)