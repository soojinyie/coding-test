import sys
input = sys.stdin.readline

n, x = map(int, input().split())

수열 = map(int,input().split())

for number in 수열 :
    if (number < x): print(number, end=' ')