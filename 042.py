import sys

k=int(input())
MOD=10**9+7

#kが9の倍数でないとき
if k % 9:
    print(0)
    sys.exit()
#dp[整数の桁和]=通り数
dp=[0]*(k+1)
dp[0]=1
for i in range(1,k+1):
    b=min(i,9)
    for j in range(b):
        dp[i] += dp[i-j-1]
        #dp[i]=dp[i-1]+dp[i-2]+...+dp[i-9]
    dp[i]=dp[i]%MOD
    #print(i,b,dp[i])

print(dp[k])