#TLEくらう.

#from collections import deque
import sys
sys.setrecursionlimit(50000)
n=int(input())

#1-indexedに対応
graph=[[] for _ in range(n+1)]

for i in range(n-1):
    a,b=map(int,input().split())

    graph[a].append(b)
    graph[b].append(a)

#彩色問題をDFSで
col=[-1]*(n+1)

def dfs(pos,cur):
    col[pos]=cur

    for i in graph[pos]:
        if col[i] ==-1:
            dfs(i,1-cur)

dfs(1,0)

#print(col)
d_even=0
for i in range(1,n+1):
    if col[i] % 2 == 0:
        d_even+=1

ans=[]
for i in range(1,n+1):
    if d_even >= n//2 and col[i] % 2==0:
        ans.append(i)
    elif d_even < n//2 and col[i] % 2 ==1:
        ans.append(i)
for i in ans[:n//2]:
    print(i,end=" ")