a, b=map(int, input().split())
box=[0]*a

for c in range(b):
    i,j,k=map(int, input().split())
    for bo in range(i, j+1):
        box[bo-1]=k

for i in range(a):
    print(box[i],end=' ')