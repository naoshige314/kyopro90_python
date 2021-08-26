n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort()

cnt=0

for i in range(n):
    cnt+= abs(a[i]-b[i])

print(cnt)