#連続するピースの選び方＝始点と終点を探索
#Nと1がつながってるので、終点始点をまたぐ取り方を試すため、
#全体を2周する

import sys
n=int(input())
a=list(map(int,input().split()))

S=sum(a)
if S%10:#10で割り切れないとき10分割できない
    print('No')
    sys.exit()

#区間[i,j]の和を保持しつつ検索
cur=0
i=0
tar=S//10
for j in range(2*n):
    cur += a[j%n]
    #print(i,j,cur)
    while cur > tar:#1/10超えてる間
        cur -= a[i%n]#中身を減らしてから
        i += 1#始点を進める
        #print(i,j,cur)
    
    if cur == tar:#条件満たせば終了
        print('Yes')
        sys.exit()

print('No')

    