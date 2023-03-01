
# Q1) 큰 수의 법칙

pre_condition = input()
target_list = input()

N_M_K_list = list(map(int,pre_condition.split()))
N = N_M_K_list[0]
M = N_M_K_list[1]
K = N_M_K_list[2]

list_original = list(map(int, target_list.split()))

# 이 짓거리를 하지않고 간단히 정렬을 사용하면 해결된다
list_largest_value = max(list_original)
list_second = list_original.copy()
list_second.remove(list_largest_value)
list_second_large_value = max(list_second)

count = 0
largest_number = 0

# 일일히 카운트하지 않고 K번을 얼마나 반복할 수 있냐를 계산하여 풀 수도 있음
if N == len(list_original):
    while count < M:
        for i in range(K):
            largest_number += list_largest_value
            count = count + 1

            if count == M:
                print(largest_number)
                exit()

        largest_number += list_second_large_value
        count = count + 1
else:
    print("wrong condition")