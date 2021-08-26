#TLE
import sys
sys.setrecursionlimit(100000)
n,l=map(int,input().split())
MOD=10**9+7
#L段飛ばしを最高何回できるか
m=n//l

nCr = {}
def cmb_mod(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = (cmb_mod(n-1,r) + cmb_mod(n-1,r-1))%MOD
    return nCr[(n,r)]



ans=1
for i in range(1,m+1):
    t=n-i*l#1段のぼる回数
    ans += cmb_mod(t+i,i)
    ans= ans%MOD

print(ans)



