n=int(input())

#bit全探索

for i in range(1<<(n-1)):
    cnt_1 = - n // 2 #1の数
    cnt_2 = 0#()が閉じてるかどうか
    ok=True
    for j in range(n):
        k=n-1-j
        if (i>>k) & 1:
            cnt_1 += 1
            cnt_2 -= 1
        else:
            cnt_2 += 1
        if cnt_2 < 0:
            ok=False
    
    if cnt_1 == 0 and ok:
        S=[]
        for j in range(n):
            k=n-1-j
            if (i>>k) & 1:
                S.append(')')
            else:
                S.append('(')
        print(''.join(S))