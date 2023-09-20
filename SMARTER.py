# cook your dish here
import math
for t in range(int(input())):
    l,ts,hs=map(int,input().split())
    time_by_t = math.ceil(l/ts) 
    
    time_by_h = math.ceil(l/hs)
    
    
    print(time_by_t-time_by_h - 1)
 
