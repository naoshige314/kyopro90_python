n=int(input())

H=1000
W=1000

s=[[0]*(W+2) for _ in range(H+2)]
k=[0]*(n+1)

for i in range(n):
    lx,ly,rx,ry=map(int,input().split())
    
    s[ly][lx] += 1
    s[ly][rx] -= 1
    s[ry][lx] -= 1
    s[ry][rx] += 1

#print(s)

#2dいもす法
#x方向の累積和
for y in range(H+1):
    for x in range(W+1):
        if x == 0:
            continue
        s[y][x] += s[y][x-1]

#print(s)

#y方向の累積和
for x in range(W+1):
    for y in range(H+1):
        if y == 0:
            continue
        s[y][x] += s[y-1][x]

for y in range(H+1):
    for x in range(W+1):
        #kの該当部分を足す
        k[s[y][x]] += 1

#print(s)

for i in range(1,n+1):
    print(k[i])

#print(s)