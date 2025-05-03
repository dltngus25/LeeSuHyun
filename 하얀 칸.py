import sys
input=sys.stdin.readline
chess=[]
count=0

while True:
    N_T,M_T=map(int,input().split())
    for i in range(N_T):
        N=int(input())
    for i in range(M_T):
        M=int(input())
    
    if N_T==0 and M_T==0:
        break
print(len(N&M))for i in range(8):
    chess.append(input()) # 채스판 형태 입력

for x in range(8):
    for y in range(8):
        if x%2 ==0 and y%2 ==0 and chess[x][y]=='F': # 짝수줄 짝수칸에 F면 
            count+=1
        if x%2!=0 and y%2 !=0 and chess[x][y]=='F': # 홀수줄 홀수칸에 F면
            count+=1
print(count)