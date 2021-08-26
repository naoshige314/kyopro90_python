#import bisect
#a=[10,20,30,30,30,40,50,60]
#bl=bisect.bisect_left(a,30)
#br=bisect.bisect_right(a,30)
#print(bl,br) 2 5

N,L=map(int,input().split())
K=int(input())
A=list(map(int,input().split()))


left=0
right=L

while right-left > 1:
    mid=(right+left)//2#mid cm以上の長さのものがK+1個作れるか

    #貪欲法でようかんを切る
    cur=0#今のようかんの長さ
    num=0#切れたようかんの個数
    for i in range(N):
        if i == 0:
            d=A[0]
        else:
            d=A[i]-A[i-1]
        
        if cur + d >= mid:
            cur=0
            num+=1
        else:
            cur += d
    
    #右端の切れ端
    d=L-A[-1]
    if cur + d >= mid:
        num += 1
    #右端が基準を超えていれば個数＋１、
    #超えてなければ余りはその前のようかんと一緒のブロックになる
    
    #print(left,mid,right,num)
    #ansまではOK、ans+1からはNGになる
    if num >= (K+1):#OKだった場合
        left = mid
    else:
        right = mid
    
    
    

print(left)
