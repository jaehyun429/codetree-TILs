m1, d1, m2, d2 = map(int, input().split())
A = input()
#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def Days (m, d):
    sum_of_days = 0
    for i in range(1, m):
        sum_of_days += num_of_days[i]
    
    sum_of_days += d
    return sum_of_days

diff = (Days(m2, d2) - Days(m1, d1))
quote_diff = diff//7
remain_diff = diff%7

if days.index(A) <= remain_diff:
    print(quote_diff+1)
else:
    print(quote_diff)
