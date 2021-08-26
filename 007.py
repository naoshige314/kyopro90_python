import bisect

n=int(input())
a=list(map(int,input().split()))
q=int(input())

a.sort()
#print(a)

for i in range(q):
    ans=0
    b=int(input())
    cnt=bisect.bisect_left(a,b)
    if cnt == 0:
        ans=abs(a[0]-b)
    elif cnt == n:
        ans=abs(a[n-1]-b)
    else:
        ans=min(abs(a[cnt]-b),abs(a[cnt-1]-b))
    print(ans)
