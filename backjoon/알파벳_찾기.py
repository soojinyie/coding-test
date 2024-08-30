import sys
input = sys.stdin.readline

word = input().strip()

for alphababet in 'abcdefghijklmnopqrstuvwxyz':
    print(word.find(alphababet), end=' ')