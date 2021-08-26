n,k=map(int,input().split())
a=list(map(int,input().split()))

#参照dictと長さを記録するlen
d=dict()
l=0

#iからjを見る尺取り法
i=0
ans = 0
for j in range(n):
    aj=a[j]
    if aj in d:#dictの場合、inはO(1)で高速
        d[aj] += 1
    else:
        d[aj] = 1
        l += 1
    
    #lenがkを超えると、lenを短くするようにiを動かす
    while l > k:
        ai=a[i]
        d[ai] -= 1
        i += 1
        if d[ai] == 0:
            d.pop(ai)
            l -= 1
    
    ans = max(ans, j-i+1)#iからjまで（両端含む)

print(ans)




