from collections import deque

q=int(input())
d=deque()
for i in range(q):
    t,x=map(int,input().split())
    if t==1:
        d.appendleft(x)
    elif t==2:
        d.append(x)
    else:
        print(d[x-1])
