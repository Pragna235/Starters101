# cook your dish here
def min_moves(n,m,s,k):
    minMoves = float('inf')
    
    for i in range(n):
        moves=0
        for j in range(m):
            diff = int(k[j]) - int(s[(i+j) % n])
            if diff<-5:
                diff+=10
            elif diff>5:
                diff-=10
            moves+=abs(diff) 
        minMoves = min(minMoves,moves)
    return minMoves

for t in range(int(input())):
    n,m=map(int,input().split())
    string = input()
    key = input()
    print(min_moves(n,m,string,key))
    
    