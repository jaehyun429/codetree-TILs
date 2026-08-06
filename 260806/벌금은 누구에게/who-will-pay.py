n, m, k = map(int, input().split())

students = [0]* 101

result = -1
for i in range(m):
    num = int(input())
    students[num] += 1
    if students[num] >= k:
        result = num
        break
     

print(result)