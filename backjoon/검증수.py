import sys
input = sys.stdin.readline

numbers = map(int, input().split())

result = 0
for n in numbers:
    result += n*n
    
print(result%10)