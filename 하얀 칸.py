import sys
input=sys.stdin.readline

while True:
    N_T,M_T=map(int,input().split())
    for i in range(N_T):
        N=int(input())
    for i in range(M_T):
        M=int(input())
    
    if N_T==0 and M_T==0:
        break
print(len(N&M))