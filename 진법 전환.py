nums = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n, b = input().split()

ans = 0

for i, num in enumerate(n[::-1]):
    ans += int(b) ** i * nums.index(num)

print(ans)