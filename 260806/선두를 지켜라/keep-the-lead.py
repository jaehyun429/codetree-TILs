import sys
input = sys.stdin.readline

def run(k):
    dist = [0]                      
    for _ in range(k):
        v, t = map(int, input().split())
        for _ in range(t):
            dist.append(dist[-1] + v)
    return dist

n, m = map(int, input().split())
a = run(n)
b = run(m)

leader = 0
count = 0
for x, y in zip(a, b):
    if x == y:
        continue
    cur = 1 if x > y else -1
    if leader != 0 and cur != leader:
        count += 1
    leader = cur

print(count)