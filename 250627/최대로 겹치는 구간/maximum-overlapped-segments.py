N = int(input())



num_list = [0] * 201

for i in range (N):
    a, b = list(map(int, input().split()))
    for i in range(a+100, b+100):
        num_list[i] += 1


print(max(num_list))