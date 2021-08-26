n,q=map(int,input().split())
a=list(map(int,input().split()))

#段差の差
#後が高ければ＋、前が高ければ-
#クエリで前の影響が次以降に反映されるので、
#どこの高さが変わったか保存しておく必要あり
d=[a[i+1]-a[i] for i in range(n-1)]

#初期の不便さ
ans=0
for i in range(n-1):
    ans += abs(a[i]-a[i+1])

#クエリ
for _ in range(q):
    l,r,v=map(int,input().split())
    l -= 1
    r -= 1
    if l:
        d0=d[l-1]
        d[l-1] += v
        d1=d[l-1]
        ans += abs(d1)-abs(d0)
    if r != n-1:
        d0=d[r]
        d[r] -= v
        d1=d[r]
        ans += abs(d1)-abs(d0)
    print(ans)
