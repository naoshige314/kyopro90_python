import heapq
n,k=map(int,input().split())



q=[]
#部分点、満点-部分点の順に格納、符号を逆に
for i in range(n):
    a,b=map(int,input().split())
    c=a-b
    q.append([-b,-c])


heapq.heapify(q)

ans=0
for i in range(k):
    tmp=heapq.heappop(q)
    ans += tmp[0]
    if tmp[1]:
        heapq.heappush(q,[tmp[1],0])

print(-ans)
