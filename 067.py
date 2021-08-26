n,k=map(int,input().split())
n8=str(n)

def calc(a):
    l=len(a)
    num=0
    for i in range(l):
        num += int(a[-i-1]) * (8**i)
    num9=[]
    for i in range(20,-1,-1):
        t=(num // (9**i))%9
        if t == 8:
            t=5
        num9.append(str(t))
    snum9=''.join(num9)
    return str(int(snum9))
cur=n8
for i in range(k):
    cur=calc(cur)

print(cur)
