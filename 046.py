n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
MOD=46
#46で割った余りで分類し直し、個数を各要素に保存
am=[0]*MOD
bm=[0]*MOD
cm=[0]*MOD

for i in range(n):
    a0=a[i]%MOD
    b0=b[i]%MOD
    c0=c[i]%MOD
    am[a0] += 1
    bm[b0] += 1
    cm[c0] += 1

#print(am)
#print(bm)
#print(cm)
ans=0
#i+j+k=46m になるようkを選ぶ
#m=0,1,2かつ0<k<45なので,m=2としてk%MODをとる
#am[i]とbm[j]とcm[k]を見る
for i in range(MOD):
    for j in range(MOD):
        k=(MOD*2-(i+j))%MOD
        ans += am[i]*bm[j]*cm[k]

print(ans)
