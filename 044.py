n,q=map(int,input().split())
a=list(map(int,input().split()))

shift=0#クエリ2が呼び出された回数（数列右へシフト）

for _ in range(q):
    t,x,y=map(int,input().split())
    #0-indexedに
    x-=1
    y-=1
    if t == 1:
        tx=(x-shift)%n
        ty=(y-shift)%n
        a[tx],a[ty]=a[ty],a[tx]
    elif t == 2:
        shift += 1
    else:
        tx=(x-shift)%n
        print(a[tx])

