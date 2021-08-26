h,w=map(int,input().split())
c=[input() for _ in range(h)]

#bit全探索で通る個所を決める→
#山じゃないことを確認→
#カウント→
#始点決めて1周できるか確認

dx=[-1,0,1,0]
dy=[0,-1,0,1]
ans=-1
land=[[0]*w for _ in range(h)]#候補地
for bit in range(1<<(h*w)):
    land=[[0]*w for _ in range(h)]
    judge=[[0]*w for _ in range(h)]
    flag=True
    tmp=0
    for p in range(h*w):
        if bit & (1<<p):
            if c[p//w][p%w]=='#':
                flag=False
                break
            land[p//w][p%w]=1
            tmp += 1
    if flag and tmp > 2:
        #landの情報からjudgeを更新
        #選ばれたマス（land=1）が隣接してるかを確認
        for i in range(h):
            for j in range(w):
                for k in range(4):
                    di=i+dy[k]
                    dj=j+dx[k]
                    if di >= 0 and di < h and dj >= 0 and dj < w:
                        judge[i][j] += land[di][dj]
        
        for i in range(h):
            for j in range(w):
                #選んだマスが隣接2マスとつながってるかどうか
                if land[i][j]==1:
                    if judge[i][j]!=2:
                        flag=False
    
    if flag:
        ans=max(ans,tmp)

print(ans)