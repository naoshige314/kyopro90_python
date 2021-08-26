H,W=map(int,input().split())
p=[list(map(int,input().split())) for _ in range(H)]

ans=0
#行について選ぶ選ばないを全探索
for bit in range(1<<H):
    h_size=0
    for i in range(H):
        if bit&(1<<i):
            h_size += 1
    
    #答えを格納するリスト
    num=[0]*(H*W+1)
    for j in range(W):
        tmp=[]
        for i in range(H):
            if bit&(1<<i):#対象の列の数値を見る
                tmp.append(p[i][j])
        if len(tmp):
            a=max(tmp)
            b=min(tmp)
            if a == b:#全ての数値が同じなら
                num[a] += 1
    
    w_size = max(num)
    ans = max(ans, w_size*h_size)

print(ans)


