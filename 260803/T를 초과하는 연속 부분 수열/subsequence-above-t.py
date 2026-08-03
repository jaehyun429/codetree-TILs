n, t = map(int, input().split())

nums = list(map(int, input().split()))

cnt = 0
result = 0

for i in range(n):
    if i >=1 and nums[i] > t:
        cnt += 1
    elif i == 0 and nums[i] > t:
        cnt += 1
    else:
        cnt = 0
    
    result = max(cnt, result)
    

print(result)