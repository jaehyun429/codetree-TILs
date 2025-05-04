m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


sum_1 = d1
for i in range(1, m1):
    sum_1 += num_of_days[i]

sum_2 = d2+1
for i in range(1, m2):
    sum_2 += num_of_days[i]


print(sum_2 - sum_1)


