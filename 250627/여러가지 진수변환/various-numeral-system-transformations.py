N, B = map(int, input().split())


remain_list = []


while True :
    if N < B :
        remain_list.append(N)
        break
    remain = N % B
    N = N // B
    remain_list.append(remain)
    

remain_list.reverse()

for i in remain_list:
    print(i, end ="")
