n = int(input())

nums = [int(input()) for _ in range(n)]

cnt = 1
result = 0

for i in range(n):
    if i>= 1 and nums[i-1] < nums[i]:
        cnt += 1
    else:
        cnt = 1

    result = max(cnt, result)


print(result)