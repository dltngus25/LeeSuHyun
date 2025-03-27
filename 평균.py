a=int(input()) # 처음 과목의 갯수
b=list(map(int,input().split())) # 점수들
M=max(b) # 점수중의 최대값

for i in range(a):
    b[i]=b[i]/M*100 #본 점수/최고점*100

print(sum(b)/a) #새 점수들의 합