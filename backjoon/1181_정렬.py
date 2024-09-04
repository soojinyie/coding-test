import sys
input = sys.stdin.readline

N = int(input())

str_set = set()
for i in range (N):
    str = input().strip()
    str_set.add(str)

str_lst = list(str_set)
str_lst.sort(key=lambda x:(len(x), x))

for str in str_lst:
    print(str)