n=int(input())

#1組と2組の合計をそれぞれ累積和で保存
#1-index
c1=[0]*(n+1)
c2=[0]*(n+1)

for i in range(1,n+1):
    c,p=map(int,input().split())
    if c==1:
        c1[i] = c1[i-1] + p
        c2[i] = c2[i-1]
    else:
        c1[i] = c1[i-1]
        c2[i] = c2[i-1] + p
#print(c1)
#print(c2)
q=int(input())

for j in range(q):
    L,R=map(int,input().split())
    score1=c1[R]-c1[L-1]
    score2=c2[R]-c2[L-1]
    print(score1,score2)
