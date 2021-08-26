import itertools
n=int(input())
r=[i for i in range(n)]
#print(r)

a=[list(map(int,input().split())) for _ in range(n)]

#print(a)
m=int(input())
rumor=[[] for _ in range(n)]

for i in range(m):
    x,y=map(int,input().split())
    x -= 1
    y -= 1

    rumor[x].append(y)
    rumor[y].append(x)

INF = 1e10
ans = INF
for ite in itertools.permutations(r):
    t=0
    flag=True
    for i in range(n):
        if i:
            if ite[i] in rumor[ite[i-1]]:
                flag=False
                break
        t += a[ite[i]][i]
    
    if flag:
        ans=min(ans,t)

if ans == INF:
    print(-1)
else:
    print(ans)