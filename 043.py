from collections import deque
h,w=map(int,input().split())
rs,cs=map(int,input().split())
rt,ct=map(int,input().split())
rs-=1
cs-=1
rt-=1
ct-=1

s=[input() for _ in range(h)]

di=[-1,0,1,0]
dj=[0,-1,0,1]

INF=1001001001
#0:横向き、1:縦向きの時のdist,visited
dist=[[[INF]*w for _ in range(h)] for __ in range(2)]
visited=[[[0]*w for _ in range(h)] for __ in range(2)]
dist[0][rs][cs]=0
dist[1][rs][cs]=0
q=deque()
#横向きスタートと縦向きスタート
q.append([0,rs,cs])
q.append([1,rs,cs])

while q:
    v=q.popleft()
    i,j=v[1],v[2]
    vec=v[0]
    if visited[vec][i][j]:
        continue
    visited[vec][i][j]=1
    d=dist[vec][i][j]

    #縦横に移動
    for k in range(4):
        ni=i+di[k]
        nj=j+dj[k]
        if ni < 0 or nj < 0 or ni >= h or nj >= w:
            continue
        if s[ni][nj] == '#':
            continue
        if dist[k%2][ni][nj] <= d:
            continue
        if k%2==vec:#同じ方向のとき
            dist[k%2][ni][nj]=d
            q.appendleft([k%2,ni,nj])
        else:#違う方向のとき
            dist[k%2][ni][nj]=d+1
            q.append([k%2,ni,nj])
        #print([0,ni,nj])

print(min(dist[0][rt][ct],dist[1][rt][ct]))