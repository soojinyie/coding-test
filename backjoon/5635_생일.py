from datetime import date
import sys
input = sys.stdin.readline

N = int(input())
student_lst = []
for i in range (N):
    name, dd, mm, yyyy = input().split()
    days_from_birth = date.today() - date(int(yyyy), int(mm), int(dd))
    student_lst.append([name, days_from_birth])
    # 숫자를 정렬할 때에는 반드시 int 타입으로 변환 후 정렬하기. string 타입일 경우 '11' 이 '9' 보다 작다.

student_lst.sort(key=lambda x:(x[1]))

print(student_lst[0][0])
print(student_lst[-1][0])