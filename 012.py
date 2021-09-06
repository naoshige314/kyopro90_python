class UnionFind:
    def __init__(self,n):
        self.par=[-1]*n
        self.siz=[1]*n
    
    #根を求める
    def root(self,x):
        if self.par[x] == -1:
            return x
        else:
            #経路圧縮
            self.par[x]=self.root(self.par[x])
            return self.par[x]
    
    #グループ判定(根が一致するかどうか)
    def issame(self,x,y):
        return self.root(x) == self.root(y)
    
    #xとyを併合する
    def unite(self,x,y):
        #根まで移動する
        x=self.root(x)
        y=self.root(y)

        if x==y:
            return False

        #union by size(y側のサイズを小さく)
        if self.siz[x] < self.siz[y]:
            tmp=y
            y=x
            x=tmp
        
        self.par[y]=x
        self.siz[x] += self.siz[y]
        return True
    
    #xを含むグループのサイズ
    def size(self,x):
        return self.siz[self.root(x)]

#各座標を要素としたUnionFindに加えて
#各座標が赤く塗られているかどうかを保存しておく

H,W=map(int,input().split())
Q=int(input())

#上からi,左からjのindexはi*W+j
uf=UnionFind(H*W)

#上下左右
dx=[1,0,-1,0]
dy=[0,1,0,-1]

painted=[[False]*W for _ in range(H)]

def index(i,j):
    return i*W+j


for _ in range(Q):
    query=list(map(int,input().split()))
    if query[0] == 1:
        #0-indexedに
        r=query[1]-1
        c=query[2]-1
        #赤く塗る
        painted[r][c]=True
        #ufを更新
        for k in range(4):
            i=r+dy[k]
            j=c+dx[k]
            if i < 0 or i == H or j < 0 or j == W:
                continue
            if painted[i][j]:#赤色続きならufくっつける
                uf.unite(index(r,c),index(i,j))

    else:
        ra,ca,rb,cb=query[1]-1,query[2]-1,query[3]-1,query[4]-1
        #答えの出力
        #同じマスの場合
        if ra==rb and ca == cb:
            if painted[ra][ca]:
                print('Yes')
            else:
                print('No')
        #違うマスの場合
        elif uf.issame(index(ra,ca),index(rb,cb)):
            print('Yes')
        else:
            print('No')


