h,w=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(h)]
b=[list(map(int,input().split())) for _ in range(h)]

#上から順に決めて行けばOK
#0<=x<h-1,0<=y<w-1の全マスを合わせて、
#x=h-1,y=w-1がaとbで合ってたらOK

ans=0

dx=[0,1,0,1]
dy=[0,0,1,1]

def calc(x,y,p):
    for k in range(4):
        xx=x+dx[k]
        yy=y+dy[k]
        a[xx][yy] += p

for x in range(h-1):
    for y in range(w-1):
        diff=b[x][y]-a[x][y]
        calc(x,y,diff)
        ans += abs(diff)

#判定
flag=True
for x in range(h):
    if b[x][w-1]-a[x][w-1]:
        flag=False

for y in range(w):
    if b[h-1][y]-a[h-1][y]:
        flag=False

if flag:
    print('Yes')
    print(ans)
else:
    print('No')