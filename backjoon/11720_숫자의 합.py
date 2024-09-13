import sys
input = sys.stdin.readline

N = int(input())
num_lst = list(input().strip())

res = 0
for num in num_lst:
    res += int(num)

print(res)
