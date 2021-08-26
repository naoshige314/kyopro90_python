import math
T=int(input())
L,X,Y=map(int,input().split())

q=int(input())

r=L/2

def theta(e):
    return -e/T*2*math.pi-math.pi/2

def y_c(time):
    return r*math.cos(theta(time))

def z_c(time):
    return r*math.sin(theta(time))+r

def dist(y):
    return math.sqrt(X*X+(Y-y)*(Y-y))

for i in range(q):
    e=int(input())
    y=y_c(e)
    z=z_c(e)
    #print(0,y,z)
    print(math.degrees(math.atan2(z,dist(y))))


