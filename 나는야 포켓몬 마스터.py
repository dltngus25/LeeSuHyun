import sys
input=sys.stdin.readline

N,M=map(int,input().split())
pl={}

for i in range(1, N+1):
    a = input().rstrip()
    pl[i]=a
    pl[a]=i

for i in range(M):
    answer=input().rstrip()
    if answer.isdigit(): print(pl[int(answer)])
    else: print(pl[answer])