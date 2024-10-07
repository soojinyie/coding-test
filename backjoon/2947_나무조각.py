num_lst = list(map(int, input().split()))

while num_lst != [1,2,3,4,5]:
    for i in range (4):
        if num_lst[i] > num_lst[i+1]:
            num_lst[i], num_lst[i+1] = num_lst[i+1], num_lst[i]
            for num in num_lst:
                print(num, end=' ')
            print()
