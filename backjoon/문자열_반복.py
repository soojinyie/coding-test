import sys
input = sys.stdin.readline

t = int(input())

for tc in range (t):
    r, s = input().rstrip().split()
    if tc != 0: print()
    for letter in s:
        print(letter*int(r), end='')
    