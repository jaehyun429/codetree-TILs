import math

N = input()
# Please write your code here. 이진수 N을 받아 십진수로 변환 이후 17배 한 뒤 다시 이진수로 변환

reverse_N = "".join(reversed(N))
sum = 0

for i in range(0, len(N)):
    sum += (int(math.pow(2, i)) * int(reverse_N[i]))


sum = sum * 17

remain_list = []

while True:
    if sum < 2:
        remain_list.append(sum)
        break
    
    remain = sum % 2
    sum = sum // 2
    remain_list.append(remain)


remain_list.reverse()

for i in remain_list:
    print(i, end = "")