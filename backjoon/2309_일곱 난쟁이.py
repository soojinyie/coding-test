# from itertools import combinations

# num_lst = []
# for _ in range (9):
#     num_lst.append(int(input()))

# comb_lst = set(combinations(num_lst, 7))

# for comb in comb_lst:
#     if sum(comb) == 100:
#         dwarf_lst = list(comb)
#         dwarf_lst.sort()
#         for dwarf in dwarf_lst:
#             print(dwarf)
#         break


# num_lst = []
# sum = 0
# for i in range (9):
#     num = int(input())
#     num_lst.append(num)
#     sum += num

# target_num = sum - 100

# num_set = set()
# for i in range (9):
#     cur_num = num_lst[i]
#     searching_num = target_num - cur_num
#     if searching_num in num_set:
#         num_lst.remove(cur_num)
#         num_lst.remove(searching_num)
#         num_lst.sort()
#         for num in num_lst:
#             print(num)
#         break
#     else:
#         num_set.add(cur_num)


# num_lst = []
# sum = 0
# for i in range (9):
#     num = int(input())
#     num_lst.append(num)
#     sum += num

# target_num = sum - 100

# for i in range (9):
#     cur_num = num_lst[i]
#     searching_num = target_num - cur_num
#     if searching_num in num_lst[i+1:]:
#         num_lst.remove(cur_num)
#         num_lst.remove(searching_num)
#         num_lst.sort()
#         for num in num_lst:
#             print(num)
#         break

num_lst = []
sum = 0
for i in range (9):
    num = int(input())
    num_lst.append(num)
    sum += num

num_lst.sort()
target_num = sum - 100
found = False

for i in range (9):

    if found: #정답을 찾았다면 for 문을 탈출
        break
    cur_num = num_lst[i]
    searching_num = target_num - cur_num
    for j in range (i+1, 9):
        if num_lst[j] == searching_num:
            for k in range (9):
                if k !=i and k!=j:
                    print(num_lst[k])
            found = True
            break