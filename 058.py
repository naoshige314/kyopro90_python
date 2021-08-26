n,k=map(int,input().split())
MOD=10**5
vis=[False]*MOD

def calc(x):
    a=x//(10**4)
    b=(x//10**3)%10
    c=(x//10**2)%10
    d=(x//10)%10
    e=x%10
    return (x+a+b+c+d+e)%MOD


#初期位置
cur=n
ans_loop=[]
cnt=0
while vis[cur]==False:
    vis[cur]=True
    ans_loop.append(cur)
    cur=calc(cur)
    cnt += 1

#ループの入りの部分を求める
s=ans_loop.index(cur)
cycle=cnt-s

if k <= s:#ループに入る前の枝にいる場合
    pos=k
else:#ループ内のどこかにいる場合
    pos=s+(k-s)%cycle

print(ans_loop[pos])