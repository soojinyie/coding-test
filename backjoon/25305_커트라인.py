import sys
input = sys.stdin.readline

N, k = map(int, input().split())

score_lst = list(map(int, input().split()))

score_lst.sort(reverse=True)

print(score_lst[k-1])