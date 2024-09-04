## [case 1: 정규식 활용]
# import sys
# import re
# input = sys.stdin.readline

# regex = re.compile('[0-9]*6{3,}[0-9]*')

# num_lst = []

# i = 666
# while True:
#     if regex.match(str(i)) != None :
#         num_lst.append(i)
#     i=i+1
#     if len(num_lst) == 10000:
#         break

# n = int(input())
# print(num_lst[n-1])

## [case 2: in 문자열 활용]
import sys
import re
input = sys.stdin.readline

num_lst = []

i = 666
while True:
    if '666' in str(i):
        num_lst.append(i)
    i=i+1
    if len(num_lst) == 10000:
        break

n = int(input())
print(num_lst[n-1])