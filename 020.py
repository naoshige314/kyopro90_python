a,b,c=map(int,input().split())

m=1
flag=False

for _ in range(b):
    m=m*c
    if a < m:
        flag=True

if flag:
    print('Yes')
else:
    print('No')