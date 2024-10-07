import sys
input = sys.stdin.readline

N = int(input())
member_lst = []
for i in range (N):
    age, name = input().split()
    member_lst.append([int(age), name, i])
    # 숫자를 정렬할 때에는 반드시 int 타입으로 변환 후 정렬하기. string 타입일 경우 '11' 이 '9' 보다 작다.

member_lst.sort(key=lambda x:(x[0], x[2]))

for member in member_lst:
    print(member[0], member[1])