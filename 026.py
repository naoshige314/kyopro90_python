from collections import deque
n=int(input())

#1-indexedに対応
graph=[[] for _ in range(n+1)]

for i in range(n-1):
    a,b=map(int,input().split())

    graph[a].append(b)
    graph[b].append(a)

dist=[-1]*(n+1)
dist[1]=0
dist[0]=0
#-1が未訪問

d=deque()
d.append(1)#頂点1を訪問

while d:
    #print(d)
    v=d.popleft()#要素の左端を削除して取得
    for i in graph[v]:
        if dist[i] != -1:#訪問済みであれば
            continue
        dist[i]=dist[v] + 1 #未訪問ならdistを計算 今いる場所の隣なので+1
        d.append(i)#今回新しく見つけた頂点を追加
    #print(d)
#for i in range(1,n+1):
#    print(i,dist[i])

d_even=0
for i in range(1,n+1):
    if dist[i] % 2 == 0:
        d_even+=1

ans=[]
for i in range(1,n+1):
    if d_even >= n//2 and dist[i] % 2==0:
        ans.append(i)
    elif d_even < n//2 and dist[i] % 2 ==1:
        ans.append(i)
for i in ans[:n//2]:
    print(i,end=" ")


