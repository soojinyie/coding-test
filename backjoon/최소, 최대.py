n = int(input())
numbers = list(map(int, input().rstrip().split()))

print(min(numbers), max(numbers))