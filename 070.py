import statistics
n=int(input())
#co=[list(map(int,input().split())) for _ in range(n)]
x=[0]*n
y=[0]*n
for i in range(n):
    a,b=map(int,input().split())
    x[i]=a
    y[i]=b



def man_dist(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])


p=statistics.median_high(x)
q=statistics.median_high(y)

ans=0
for i in range(n):
    ans += man_dist([x[i],y[i]],[p,q])

print(ans)