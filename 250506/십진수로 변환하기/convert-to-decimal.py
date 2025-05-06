binary = input()

binary_list = []
for i in binary:
    binary_list.append(int(i))

num = 0

for i in range(len(binary_list)):
    num = num * 2 + binary_list[i]

print(num)

# Please write your code here.