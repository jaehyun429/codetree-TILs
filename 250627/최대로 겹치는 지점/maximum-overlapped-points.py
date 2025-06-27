N = int(input())


num_list = [0] * 100

for i in range (N):
    a, b = list(map(int, input().split()))
    for i in range(a, b+1):
        num_list[i] += 1


print(max(num_list))