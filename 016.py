n=int(input())
abc=list(map(int,input().split()))
tot=9999

abc.sort()
#print(abc)
a=abc[0]
b=abc[1]
c=abc[2]

h_c=min(tot,n//c)
h_b=min(tot,n//b)
h_a=min(tot,n//a)


#print(h_c,h_b,h_a,l_c)
ans=tot
for i in range(h_c+1):
    cur = n - i*c
    h_b=min(tot,cur//b)
    #l_b=max(0,cur-tot*a)
    for j in range(h_b+1):
        cur = n - (i * c + j * b)
        if cur < 0:
            break
        if cur % a == 0:
            ans=min(ans,i + j + cur//a)

print(ans)
