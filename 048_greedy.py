n,k=map(int,input().split())

q=[]
for _ in range(n):
    a,b=map(int,input().split())
    q.append(b)#部分点
    q.append(a-b)#満点-部分点

q.sort(reverse=True)
ans=0
for i in range(k):
    ans += q[i]

print(ans)