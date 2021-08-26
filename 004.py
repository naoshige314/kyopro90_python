H,W=map(int,input().split())

A=[0]*H
sum_r=[0]*H
sum_c=[0]*W

for i in range(H):
    A[i]=list(map(int,input().split()))

    for j in range(W):
        sum_r[i] += A[i][j]
        sum_c[j] += A[i][j]

B_tmp=[0]*W
for i in range(H):
    for j in range(W):
        B_tmp[j] = sum_r[i]+sum_c[j]-A[i][j]
    
    print(' '.join(map(str, B_tmp)))

