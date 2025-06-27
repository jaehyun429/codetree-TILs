import math

a, b = map(int, input().split())
n = input()

# Please write your code here. A진수로 표현된 n을 b진수로 변환하기


reverse_n = "".join(reversed(n))
sum = 0

for i in range (0, len(n)):
    sum += int(math.pow(a, i)) * int(reverse_n[i])

result_list = []

while True :
    if sum < b:
        result_list.append(sum)
        break

    
    remain = sum % b
    sum = sum // b

    result_list.append(remain)


result_list.reverse()

for i in result_list:
    print(i, end="")


