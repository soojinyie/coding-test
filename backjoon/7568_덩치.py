import sys
input = sys.stdin.readline

N = int(input())
person_lst = []

for _ in range (N):
    w, h = input().split()
    person_lst.append([int(w), int(h), 1])

for person in person_lst:
    for compared_person in person_lst:
        if compared_person[0] > person[0] and compared_person[1] > person[1]:
            person[2] += 1

for person in person_lst:
    print(person[2], end=' ')