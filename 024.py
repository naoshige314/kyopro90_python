n,k=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

cnt=0

for i in range(n):
    cnt += abs(a[i]-b[i])

ans=cnt-k

if ans <= 0 and ans % 2 ==0:
    print('Yes')
else:
    print('No')
