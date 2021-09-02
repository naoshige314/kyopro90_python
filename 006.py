import heapq



n,k=map(int,input().split())
#辞書順で最小のものをheapqで取り出す
#i文字目を見るとき、
#(i-1文字目に使った文字の位置)～n-i+1文字目 までが使用できる

s=input()

hs=[]
for i in range(n-k+1):
    hs.append([s[i],i])#何文字目かも同時に保存

heapq.heapify(hs)

ans=[]
#前の文字の位置
t=-1
#今何文字取ったか
l=0

while l < k:
    #辞書順最小の文字で、その文字の中で一番前にある文字をピック
    cur=heapq.heappop(hs)
    p,q=cur[0],cur[1]
    if q < t:#先に取り出した文字より前のものなら飛ばす
        continue
    #採用
    ans.append(p)
    t=q
    l += 1
    #もう一文字使えるようになった
    u=n-k+l
    if u < n:
        heapq.heappush(hs,[s[u],u])

print(''.join(ans))