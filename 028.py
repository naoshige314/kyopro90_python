n=int(input())

H=1000
W=1000

s=[[0]*(W+2) for _ in range(H+2)]
t=[[0]*(W+2) for _ in range(H+2)]
k=[0]*(n+1)

for i in range(n):
    lx,ly,rx,ry=map(int,input().split())

    for y in range(ly,ry):
        s[y][lx] += 1
        s[y][rx] -= 1

#累積和

for y in range(H+1):
    for x in range(W+1):
        if x == 0:
            t[y][x]=s[y][x]
        else:
            t[y][x]=t[y][x-1]+s[y][x]
        k[t[y][x]] += 1

for i in range(1,n+1):
    print(k[i])

#print(s)
#print(t)