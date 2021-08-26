n=int(input())
s=input()
MOD=10**9+7
dp=[[0]*7 for _ in range(n)]

ref=['a','t','c','o','d','e','r']

if s[0]==ref[0]:
    dp[0][0]=1

for i in range(1,n):
    for x in range(7):
        if x == 0 and s[i] == ref[0]:
            dp[i][0]=dp[i-1][0]+1
        elif s[i] == ref[x]:
            dp[i][x]=(dp[i-1][x-1]+dp[i-1][x])%MOD
        else:
            dp[i][x]=dp[i-1][x]

print(dp[n-1][6])