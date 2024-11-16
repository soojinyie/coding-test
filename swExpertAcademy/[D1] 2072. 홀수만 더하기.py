T = int(input())

for test_case in range(1, T + 1):
	num_lst = list(map(int, input().split()))
	sum = 0
	for num in num_lst:
		if num %2 != 0: 
			sum += num
	print(f'#{test_case} {sum}')