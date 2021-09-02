n=int(input())
s=input()

#dp[r]:0~rまでのうち、条件を満たす(l,r)の通り数
#最後をrに固定していることに注意
dp=[0]*n
for i in range(1,n):
    if s[i-1] == s[i]:
        dp[i] = dp[i-1]
    else:
        dp[i] = i
#print(dp)
#最後0～最後rまでの通り数を合算する
ans=sum(dp)
print(ans)