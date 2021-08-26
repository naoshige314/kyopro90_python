n,m=map(int,input().split())
graph=[[] for _ in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i].sort()

ans=0

for i in range(n):
    l=len(graph[i])
    if l==1:
        if graph[i][0]<i:
            ans += 1
    if l > 1:
        if graph[i][0]<i and graph[i][1] >i:
            ans += 1

print(ans)