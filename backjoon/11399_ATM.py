import sys
input = sys.stdin.readline

N = int(input())
p_lst = list(map(int, input().split()))

total = 0
p_lst.sort()

for i in range (N):
    total += sum(p_lst[0:i+1])

print(total)