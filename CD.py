'''import sys
input=sys.stdin.readline
N=[]
M=[]
while True:
    N_T,M_T=map(int,input().split())
    for i in range(N_T):
        N.append(input())
    for i in range(M_T):
        M.append(input())
    
    if N_T==0 and M_T==0:
        break
print(len(N&M)) '''


import sys
input=sys.stdin.readline
count=[]
while True:
    N,M=map(int,input().split())
    if N==0 and M==0:
        break
    N_num=set(int(input()) for _ in range(N))
    M_num=set(int(input()) for _ in range(M))
    count.append(str(len(N_num&M_num)))

print('\n'.join(count))
