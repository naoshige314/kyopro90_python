from collections import deque
#入力が1-indxなのでリスト番号も1-indに
#1-indなのでfor文の範囲も変わってることに注意

n=int(input())
graph=[[] for _ in range(n+1)]

for i in range(1,n):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#BFSを2回やる
start=1
for k in range(2):

    dist=[-1]*(n+1)
    dist[start]=0
    dist[0]=0
    #-1が未訪問

    d=deque()
    d.append(start)#開始点を訪問


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
    max_dist=max(dist)
    start=dist.index(max_dist)
    #print(k,dist,start)

print(max_dist+1)
