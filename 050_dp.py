N,L=map(int,input().split())
MOD=10**9+7
#dp[i]:i段目に到達する方法の通り数
dp=[0]*(N+1)
dp[0]=1

for i in range(1,N+1):
    if i < L:
        dp[i]=dp[i-1]
    else:
        dp[i]=dp[i-1]+dp[i-L]
    dp[i]%=MOD

print(dp[N])