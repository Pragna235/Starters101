for _ in range(int(input())):
    n,m=map(int,input().split())
    string=input()
    key=input()
    mini = float('inf')
    string+=string
    for i in range(n-m+1):
        moves = 0
        for j in range(m):
            diff1 = abs(ord(string[(i + j) % n]) - ord(key[j]))
            diff2 = 10 - diff1
            moves += min(diff1, diff2)
        
        if moves < mini:
            mini = moves
    print(mini)