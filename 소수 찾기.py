a = input()
b = 0
n = list(map(int, input().split()))

for i in n:
    s = True
    if i == 1: continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            s = False
            break
    if s: b += 1

print(b)