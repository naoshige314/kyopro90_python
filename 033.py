import sys
import math
H,W=map(int,input().split())

if H==1:
    print(W)
    sys.exit()
elif W==1:
    print(H)
    sys.exit()

h_max=math.ceil(H/2)
w_max=math.ceil(W/2)
ans=h_max*w_max
print(ans)