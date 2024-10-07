from itertools import combinations

num_lst = []
for _ in range (9):
    num_lst.append(int(input()))

comb_lst = set(combinations(num_lst, 7))

for comb in comb_lst:
    if sum(comb) == 100:
        dwarf_lst = list(comb)
        dwarf_lst.sort()
        for dwarf in dwarf_lst:
            print(dwarf)
        break