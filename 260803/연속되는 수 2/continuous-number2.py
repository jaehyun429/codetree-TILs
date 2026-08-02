n = int(input())
nums = [int(input()) for _ in range(n)]

max_count = 1
current_count =1

for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 1

print(max_count)


