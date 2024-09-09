import sys
input = sys.stdin.readline

N, M = map(int, input().split())

never_heard_set = set()
never_seen_set = set()

for i in range (N):
    name = input().strip()
    never_heard_set.add(name)

for i in range(M):
    name = input().strip()
    never_seen_set.add(name)

never_heard_seen_set = never_heard_set & never_seen_set
never_heard_seen_lst = list(never_heard_seen_set)
never_heard_seen_lst.sort()

print(len(never_heard_seen_lst))
for name in never_heard_seen_lst:
    print(name)