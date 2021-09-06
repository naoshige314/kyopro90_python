#heapを用いたダイクストラ（計算量が辺数×log頂点数）
#特定の点を通るような最短経路
#スタート→点k→ゴール
#スタートとゴールそれぞれからダイクストラを行い、各点で2つの結果を足す

import heapq

INF = 1 << 60
n,m=map(int,input().split())
#edges=[[[行先、重み]のリスト] for _ in range(頂点数)]
edges = [[] for _ in range(n)]
for i in range(m):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    #無向グラフ
    edges[a].append([b,c])
    edges[b].append([a,c])

starts=[0,n-1]

ans=[0]*n
for s in starts:
    dist = [INF]*n
    dist[s] = 0

    que = [[dist[i], i] for i in range(n)]
    heapq.heapify(que)

    while(que != []):
        d, v = que[0]
        heapq.heappop(que)
        if d > dist[v]:
            continue
        for edge in edges[v]:
            if dist[edge[0]] > dist[v] + edge[1]:
                dist[edge[0]] = dist[v] + edge[1]
                heapq.heappush(que, [dist[edge[0]], edge[0]])
    
    for j in range(n):
        ans[j] += dist[j]

for i in range(n):
    print(ans[i])